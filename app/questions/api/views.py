from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from questions.api.permissions import IsAuthorOrReadOnly
from questions.models import Question
from questions.api.serializers import QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by("created_at")
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    lookup_field = "slug"

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
