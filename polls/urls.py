from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    # ── Survey (main flow) ──
    path("", views.SurveyListView.as_view(), name="index"),
    path("survey/<int:survey_id>/", views.survey_question, name="survey_start"),
    path("survey/<int:survey_id>/question/<int:question_id>/", views.survey_question, name="survey_question"),
    path("survey/<int:survey_id>/question/<int:question_id>/vote/", views.survey_vote, name="survey_vote"),
    # /polls/survey/<id>/results/
    path("survey/<int:survey_id>/results/", views.survey_results, name="survey_results"),
    # /polls/survey/<id>/finish/
    path("survey/<int:survey_id>/finish/", views.survey_finish, name="survey_finish"),

    # ── Auth ──
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("switch/", views.user_switch, name="user_switch"),

    # ── Legacy (keep old question URLs working) ──
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
