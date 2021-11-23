from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.utils.timezone import now
from datetime import timedelta
from .models import Question

from .serializers import (
    QuestionListPageSerializer,
    QuestionDetailPageSerializer,
)


class QuestionDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()

    serializer_class = QuestionDetailPageSerializer
    lookup_url_kwarg = "question_id"


class QuestionsView(ListCreateAPIView):
    queryset = Question.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return QuestionListPageSerializer
        else:
            return QuestionDetailPageSerializer
