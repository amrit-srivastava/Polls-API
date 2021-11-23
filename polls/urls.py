from django.urls import path
from . import apiviews

app_name = "polls"
urlpatterns = [
    path(
        "<int:question_id>/",
        apiviews.QuestionDetailView.as_view(),
        name="question_detail_view",
    ),
    path("", apiviews.QuestionsView.as_view(), name="questions_view"),
]
