from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
    class UserRoleChoice(models.TextChoices):
        normal = 'N', 'normal'
        admin = 'A', 'admin'

    user_role = models.CharField(max_length=3, choices=UserRoleChoice.choices, default=UserRoleChoice.normal)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"user_role: {self.user_role}, record: {self.pk}, ( user: {self.user.username} )"
