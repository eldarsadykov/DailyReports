from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class User(AbstractUser):
    pass


class Task(models.Model):
    key = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    progress = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks',
    )

    class Meta:
        unique_together = ('user', 'key')

    def __str__(self):
        return f"{self.key} {self.name} - {self.progress}%"
