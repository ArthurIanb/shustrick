from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    image = models.ImageField(upload_to="user_images/%Y/%m/%d")
    
    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"pk": self.pk})
    
    