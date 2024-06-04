from django.db import models

class AdvModel(models.Model):
    title = models.TextField()
    adv_id = models.IntegerField()
    author = models.CharField(max_length=255)
    views = models.IntegerField()
    position = models.IntegerField()
