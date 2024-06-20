from django.db import models

class TodoItem(models.Model):
    text = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)

