from django.db import models
from django.db.models import Model

# Create your models here.
class MediaOutlet(Model):
    name = models.CharField(max_length=400,unique=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Article(Model):
    url = models.URLField()
    title = models.CharField(max_length=300)
    outlet = models.ForeignKey(MediaOutlet, on_delete=models.CASCADE)
    shares = models.IntegerField()
    views = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

