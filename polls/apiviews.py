from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.utils.timezone import now
from datetime import timedelta
from .models import Question

from .serializers import (
    QuestionListPageSerializer,
    QuestionDetailPageSerializer,
)


class QuestionDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = QuestionDetailPageSerializer
    lookup_url_kwarg = "question_id"

    def get_queryset(self):
        last_two_days = now() - timedelta(days=2)
        return Question.objects.filter(pub_date__gt=last_two_days)


class QuestionsView(ListCreateAPIView):
    queryset = Question.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return QuestionListPageSerializer
        else:
            return QuestionDetailPageSerializer
