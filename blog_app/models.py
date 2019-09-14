from django.db import models
from django.utils import timezone       # To set the Date of the Post object.


class Post(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now(), verbose_name="Created Date")

    # Meta Data
    def __str__(self):
        return self.title


