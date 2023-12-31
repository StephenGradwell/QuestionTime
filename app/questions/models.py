from django.db import models
from core.models import TimeStampedModel
from django.conf import settings
import uuid as uuid_lib


class Question(TimeStampedModel):
    content = models.CharField(max_length=240)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="questions")

    def __str__(self):
        return self.content


class Answer(TimeStampedModel):
    uuid = models.UUIDField(db_index=True, editable=False,
                            default=uuid_lib.uuid4)
    body = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                 related_name="answers")
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="answers")
    voters = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                    related_name="likes")

    def __str__(self):
        return self.author.username
