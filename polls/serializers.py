from rest_framework import serializers

from .models import Question, Choice


class QuestionChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ("id", "choice_text")


class QuestionListPageSerializer(serializers.ModelSerializer):

    was_published_recently = serializers.BooleanField(read_only=True)

    class Meta:
        model = Question
        fields = "__all__"


class QuestionDetailPageSerializer(QuestionListPageSerializer):
    choice_set = QuestionChoiceSerializer(many=True)

    def create(self, validated_data):
        choice_validated_data = validated_data.pop("choice_set")
        question = Question.objects.create(**validated_data)
        choice_set_serializer = self.fields["choice_set"]
        for each in choice_validated_data:
            each["question"] = question
        choices = choice_set_serializer.create(choice_validated_data)
        return question
