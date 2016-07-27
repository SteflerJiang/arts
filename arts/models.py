from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


# class Choice(models.Model):
#     question = models.ForeignKey(Question)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

@python_2_unicode_compatible  # only if you need to support Python 2
class User(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=20)
    gender = models.CharField(max_length=10, default="male")

    def __str__(self):
        return "user " + self.name


@python_2_unicode_compatible  # only if you need to support Python 2
class Record(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=20)
    gender = models.CharField(max_length=10, default="male")
    city = models.CharField(max_length=20, default="hangzhou")

    def __str__(self):
        return "record " + self.name
