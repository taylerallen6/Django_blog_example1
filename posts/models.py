from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
    	return "/{pk}/".format(pk=self.pk)