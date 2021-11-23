from django.urls import path
from . import apiviews

app_name = "polls"
urlpatterns = [
    path(
        "questions/<int:question_id>/",
        apiviews.QuestionDetailView.as_view(),
        name="question_detail_view",
    ),
    path("questions/", apiviews.QuestionsView.as_view(), name="questions_view"),
]
