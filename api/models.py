from django.db import models

# Create your models here.
class Message(models.Model):
    id = models.IntegerField(primary_key=True)
    ts = models.IntegerField()
    txt = models.TextField()
    sender = models.TextField()

    class Meta:
        ordering = ('id',)
