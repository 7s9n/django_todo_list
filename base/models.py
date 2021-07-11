from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse_lazy
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse_lazy('task-view' , kwargs={'pk':self.pk})
        # return reverse_lazy('task-list')
    def __str__(self):
        return self.title
