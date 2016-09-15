from __future__ import unicode_literals

from django.db import models

# Create your models here.

class loadStatus(models.Model):
    load_num = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    carrier = models.CharField(max_length=100)
    date = models.DateTimeField(blank=True, null=True)
    def __str__(self):              # __unicode__ on Python 2
        return "%s %s" % (load_num, location)

