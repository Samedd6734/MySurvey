import datetime

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db.models import F, Sum, ExpressionWrapper, Q, Case, When, BooleanField, Exists, OuterRef
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from django.utils.translation import gettext_lazy as _
from .models import Choice, Question, Survey, UserVote, UserSurveyParticipation
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.db import transaction
from django.contrib import messages


# ─────────────────────────────────────────────
# Survey (Index) View
# ─────────────────────────────────────────────

class SurveyListView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "survey_list"
    paginate_by = 8

    def get_queryset(self):
        now = timezone.now()
        
        # SQL Seviyesinde süresi bitmiş anketleri ayırt et (annotate)
        # end_date var ve timezone.now()'dan küçükse => expired
        surveys = Survey.objects.filter(pub_date__lte=now).annotate(
            is_over=Case(
                When(Q(end_date__isnull=False) & Q(end_date__lt=now), then=True),
                default=False,
                output_field=BooleanField(),
            )
        )

        if self.request.user.is_authenticated:
            surveys = surveys.annotate(
                has_completed=Exists(
                    UserSurveyParticipation.objects.filter(
                        user=self.request.user,
                        survey=OuterRef('pk')
                    )
                )
            )

        return surveys.order_by("is_over", "-pub_date")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["active_survey_count"] = Survey.objects.filter(
            Q(end_date__isnull=True) | Q(end_date__gt=now)
        ).count()
        context["total_users"] = User.objects.count()
        context["total_votes"] = Choice.objects.aggregate(s=Sum("votes"))["s"] or 0
        return context


# ─────────────────────────────────────────────
# Survey Question View (with next/prev)
# ─────────────────────────────────────────────

@login_required
def survey_question(request, survey_id, question_id=None):
    survey = get_object_or_404(Survey, pk=survey_id)

    if UserSurveyParticipation.objects.filter(user=request.user, survey=survey).exists():
        messages.warning(request, _("You have already completed this survey."))
        return HttpResponseRedirect(reverse("polls:survey_results", args=(survey.id,)))

    questions = list(survey.questions.all())

    if not questions:
        return render(request, "polls/detail.html", {
            "survey": survey,
            "error_message": _("This survey has no questions yet."),
        })

    if question_id is None:
        question = questions[0]
    else:
        question = get_object_or_404(Question, pk=question_id, survey=survey)

    idx = questions.index(question)
    prev_q = questions[idx - 1] if idx > 0 else None
    next_q = questions[idx + 1] if idx < len(questions) - 1 else None
    q_num = idx + 1
    q_total = len(questions)

    user_vote = UserVote.objects.filter(user=request.user, question=question).first()
    selected_choice_id = user_vote.choice.id if user_vote else None

    return render(request, "polls/detail.html", {
        "survey": survey,
        "question": question,
        "prev_q": prev_q,
        "next_q": next_q,
        "q_num": q_num,
        "q_total": q_total,
        "selected_choice_id": selected_choice_id,
    })


# ─────────────────────────────────────────────
# Vote
# ─────────────────────────────────────────────

@login_required
def survey_vote(request, survey_id, question_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    question = get_object_or_404(Question, pk=question_id, survey=survey)

    if UserSurveyParticipation.objects.filter(user=request.user, survey=survey).exists():
        messages.warning(request, _("You have already completed this survey."))
        return HttpResponseRedirect(reverse("polls:survey_results", args=(survey.id,)))

    questions = list(survey.questions.all())
    idx = questions.index(question)

    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        selected_choice = None

    prev_q = questions[idx - 1] if idx > 0 else None
    next_q = questions[idx + 1] if idx < len(questions) - 1 else None

    if survey.is_expired:
        return render(request, "polls/detail.html", {
            "survey": survey,
            "question": question,
            "prev_q": prev_q,
            "next_q": next_q,
            "q_num": idx + 1,
            "q_total": len(questions),
            "error_message": _("This survey has expired; you can no longer vote."),
        })

    if not selected_choice:
        return render(request, "polls/detail.html", {
            "survey": survey,
            "question": question,
            "prev_q": prev_q,
            "next_q": next_q,
            "q_num": idx + 1,
            "q_total": len(questions),
            "error_message": _("You didn't select a choice."),
        })

    with transaction.atomic():
        user_vote = UserVote.objects.filter(user=request.user, question=question).first()
        if user_vote:
            if user_vote.choice != selected_choice:
                Choice.objects.filter(pk=user_vote.choice.pk).update(votes=F("votes") - 1)
                Choice.objects.filter(pk=selected_choice.pk).update(votes=F("votes") + 1)
                user_vote.choice = selected_choice
                user_vote.save()
        else:
            Choice.objects.filter(pk=selected_choice.pk).update(votes=F("votes") + 1)
            UserVote.objects.create(user=request.user, question=question, choice=selected_choice)

    # Go to next question, or results if this was the last
    if idx < len(questions) - 1:
        next_q = questions[idx + 1]
        return HttpResponseRedirect(
            reverse("polls:survey_question", args=(survey.id, next_q.id))
        )
    return HttpResponseRedirect(
        reverse("polls:survey_results", args=(survey.id,))
    )


# ─────────────────────────────────────────────
# Survey Results
# ─────────────────────────────────────────────

@login_required
def survey_results(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    has_completed = UserSurveyParticipation.objects.filter(user=request.user, survey=survey).exists()
    questions_data = []
    for question in survey.questions.all():
        total = question.total_votes
        choices_with_pct = []
        
        # Determine highest votes for "Leading" badge
        max_votes = 0
        for choice in question.choice_set.all():
            if choice.votes > max_votes:
                max_votes = choice.votes

        for choice in question.choice_set.all():
            # Calculate percentage formatted string with dot
            pct_val = (choice.votes / total * 100) if total > 0 else 0
            is_leading = (choice.votes == max_votes) and (max_votes > 0)
            
            choices_with_pct.append({
                "choice": choice, 
                "percentage": pct_val,
                "is_leading": is_leading
            })

        questions_data.append({
            "question": question,
            "choices_with_pct": choices_with_pct,
            "total_votes": total,
        })
    return render(request, "polls/results.html", {
        "survey": survey,
        "questions_data": questions_data,
        "has_completed": has_completed,
    })

@login_required
@require_POST
def survey_finish(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    UserSurveyParticipation.objects.get_or_create(user=request.user, survey=survey)
    messages.success(request, _("You have successfully completed the survey."))
    return HttpResponseRedirect(reverse("polls:survey_results", args=(survey.id,)))



# ─────────────────────────────────────────────
# Auth Views
# ─────────────────────────────────────────────

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("polls:index")
    else:
        form = UserCreationForm()
    return render(request, "polls/register.html", {"form": form})


def login_view(request):
    error = None
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(request.GET.get("next", "polls:index"))
        else:
            error = _("Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "polls/login.html", {"form": form, "error": error})


def logout_view(request):
    logout(request)
    return redirect("polls:index")


def user_switch(request):
    """Dedicated user info / switch page."""
    return render(request, "polls/user_switch.html", {
        "current_user": request.user,
    })


# ─────────────────────────────────────────────
# Legacy redirect stubs (keep old URL working)
# ─────────────────────────────────────────────

class IndexView(generic.ListView):
    """Redirect old /polls/ to SurveyListView."""
    template_name = "polls/index.html"
    context_object_name = "survey_list"

    paginate_by = 8

    def get_queryset(self):
        now = timezone.now()
        return Survey.objects.filter(pub_date__lte=now).annotate(
            is_over=Case(
                When(Q(end_date__isnull=False) & Q(end_date__lt=now), then=True),
                default=False,
                output_field=BooleanField(),
            )
        ).order_by("is_over", "-pub_date")


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = self.object
        total = question.total_votes
        choices_with_pct = []
        
        max_votes = 0
        for choice in question.choice_set.all():
            if choice.votes > max_votes:
                max_votes = choice.votes

        for choice in question.choice_set.all():
            pct_val = (choice.votes / total * 100) if total > 0 else 0
            is_leading = (choice.votes == max_votes) and (max_votes > 0)
            choices_with_pct.append({
                "choice": choice, 
                "percentage": pct_val,
                "is_leading": is_leading
            })
        context["choices_with_pct"] = choices_with_pct
        context["total_votes"] = total
        return context


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": _("You didn't select a choice."),
        })
    selected_choice.votes = F("votes") + 1
    selected_choice.save()
    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
