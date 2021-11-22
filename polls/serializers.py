from rest_framework import serializers

from .models import Question, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ("choice_text",)


# class ChoiceSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     choice_text = serializers.CharField(max_length=200)

#     def create(self, validated_data):
#         return Choice.objects.create(**validated_data)


class ChoiceSerializerWithVotes(ChoiceSerializer):
    votes = serializers.IntegerField(read_only=True)


# class QuestionListPageSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     question_text = serializers.CharField(max_length=200)
#     pub_date = serializers.DateTimeField()
#     was_published_recently = serializers.BooleanField(
#         read_only=True
#     )  # Serializer is smart enough to understand that was_published_recently is a method on Question
#     choices = ChoiceSerializer(many=True, write_only=True)

#     def create(self, validated_data):
#         choices = validated_data.pop("choices", [])
#         question = Question.objects.create(**validated_data)
#         for choice_dict in choices:
#             choice_dict["question"] = question
#             Choice.objects.create(**choice_dict)
#         return question


class QuestionListPageSerializer(serializers.ModelSerializer):

    was_published_recently = serializers.BooleanField(read_only=True)

    class Meta:
        model = Question
        fields = "__all__"


class QuestionDetailPageSerializer(QuestionListPageSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)


class QuestionDetailPageSerializer(QuestionListPageSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)


class QuestionResultPageSerializer(QuestionListPageSerializer):
    choices = ChoiceSerializerWithVotes(many=True, read_only=True)


class VoteSerializer(serializers.Serializer):
    choice_id = serializers.IntegerField()
