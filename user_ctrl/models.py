from django.db import models
from django.contrib.auth.models import User
from group.models import Group

class pfuser(models.Model):
    User = models.OneToOneField(User, primary_key=True)
    groups = models.ManyToManyField(Group)
    groups_apply = models.ManyToManyField(Group)
    groups_staff = models.ManyToManyField(Group)

    def __unicode__(self):
        return self.User.username