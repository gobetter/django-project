from django.db import models
from django.urls import reverse

class Destination(models.Model):
    title       = models.CharField(max_length=120)
    content     = models.TextField()
    active      = models.BooleanField(default=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("destinations:destination-detail", kwargs={"id": self.id})
