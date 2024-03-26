from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Article(models.Model):
    title = models.CharField(verbose_name="title", max_length=100, null=False, blank=False)
    content = models.TextField(verbose_name="content", null=True, blank=True)
    is_published = models.BooleanField(verbose_name="is_published")
    creator = models.ForeignKey(to=get_user_model(), on_delete=models.DO_NOTHING, null=True)

    def get_absolute_url(self):
        return reverse("articles:detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title
    