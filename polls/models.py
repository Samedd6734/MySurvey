import datetime

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Survey(models.Model):
    """A Survey groups multiple Questions together."""
    title = models.CharField(max_length=200, verbose_name=_("title"))
    description = models.TextField(blank=True, verbose_name=_("description"))
    pub_date = models.DateTimeField(_("publication date"))
    end_date = models.DateTimeField(
        null=True, 
        blank=True, 
        verbose_name=_("end date"),
        help_text=_("The end date is optional. If left empty, the survey will run indefinitely.")
    )

    class Meta:
        ordering = ["-pub_date"]
        verbose_name = _("survey")
        verbose_name_plural = _("surveys")

    def __str__(self):
        return self.title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    @property
    def question_count(self):
        return self.questions.count()

    @property
    def is_expired(self):
        if self.end_date:
            return timezone.now() > self.end_date
        return False

    @property
    def total_votes(self):
        return sum(q.total_votes for q in self.questions.all())


class Question(models.Model):
    """A single question within a Survey."""
    survey = models.ForeignKey(
        Survey,
        on_delete=models.CASCADE,
        related_name="questions",
        null=True,
        blank=True,
        verbose_name=_("survey"),
    )
    question_text = models.CharField(max_length=200, verbose_name=_("question text"))
    pub_date = models.DateTimeField(_("publication date"), null=True, blank=True)

    class Meta:
        ordering = ["id"]
        verbose_name = _("question")
        verbose_name_plural = _("questions")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        if not self.pub_date:
            return False
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    @property
    def total_votes(self):
        return sum(choice.votes for choice in self.choice_set.all())


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name=_("question"))
    choice_text = models.CharField(max_length=200, verbose_name=_("choice text"))
    votes = models.IntegerField(default=0, verbose_name=_("votes"))

    class Meta:
        verbose_name = _("choice")
        verbose_name_plural = _("choices")

    def __str__(self):
        return self.choice_text


class UserVote(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name=_("user"))
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name=_("question"))
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, verbose_name=_("choice"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated at"))

    class Meta:
        unique_together = ('user', 'question')
        verbose_name = _("user vote")
        verbose_name_plural = _("user votes")

    def __str__(self):
        return f"{self.user.username} - {self.question.question_text}"


class UserSurveyParticipation(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name=_("user"))
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, verbose_name=_("survey"))
    completed_at = models.DateTimeField(auto_now_add=True, verbose_name=_("completed at"))

    class Meta:
        unique_together = ('user', 'survey')
        verbose_name = _("user survey participation")
        verbose_name_plural = _("user survey participations")

    def __str__(self):
        return f"{self.user.username} - {self.survey.title} (Completed)"
