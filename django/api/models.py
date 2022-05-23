from django.db import models
import uuid


class BaseModel(models.Model):
    """
    Abstract base class that provides a blueprint for all models.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    class Meta:
        abstract = True


class Person(BaseModel):

    full_name = models.CharField('Full Name', max_length=100, blank=True)
    preferred_name = models.CharField('Preferred Name', max_length=100)

    def __str__(self):
        return self.preferred_name
