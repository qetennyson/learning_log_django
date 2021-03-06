# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Topic(models.Model):
    """ a topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        """ return a string representation of the model"""
        return self.text


class Entry(models.Model):
    """ Something specific learned about a topic """
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __unicode__(self):
        """ Return a string representation of the model """
        if len(str(self.text)) >= 50:
            return self.text[:50] + "..."
        else:
            return self.text
