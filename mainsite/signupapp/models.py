from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserTable(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userinfo")
    isprofessor = models.BooleanField()
    university = models.CharField(max_length=200)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.user.username