from rest_framework import serializers
from datetime import datetime
import pytz

from .models import Question, Choice


class QuestionChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ("id", "choice_text")


class QuestionListPageSerializer(serializers.ModelSerializer):

    was_published_recently = serializers.BooleanField(read_only=True)
    pub_date = serializers.CharField(max_length=200)

    class Meta:
        model = Question
        fields = "__all__"


class QuestionDetailPageSerializer(QuestionListPageSerializer):
    choice_set = QuestionChoiceSerializer(many=True)

    def create(self, validated_data):
        choice_validated_data = validated_data.pop("choice_set")
        validated_data['pub_date'] = datetime.strptime(validated_data['pub_date'], '%d/%m/%Y').replace(tzinfo=pytz.utc)
        question = Question.objects.create(**validated_data)
        for each in choice_validated_data:
            each["question"] = question
            Choice.objects.create(**each)
        return question
