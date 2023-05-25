from django.db import models

# Create your models here.

class SportStream(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    stream_url = models.URLField()
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/')

    def __str__(self):
        return self.title