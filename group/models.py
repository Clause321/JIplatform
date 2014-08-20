from django.db import models

class Group(models.Model):
    name = models.CharField(max_length = 30) # Chinese name
    title = models.CharField(max_length = 30) # English title, for url use
    nature = models.CharField(max_length = 30) # department or club or other
