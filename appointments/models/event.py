from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

class Event(models.Model):
    TIME_CHOICES=(('1','9.00-10.00'),
    ('2','10.00-11.00'),
    ('3','11.00-12.00'))
    start_date = models.DateField(
      blank=False)
    start_time = MultiSelectField(choices=TIME_CHOICES,
    max_choices=1,
    blank=False,
    default='')
    end_date = models.DateField(
      blank=False)
    end_time = MultiSelectField(choices=TIME_CHOICES, max_choices=1,blank=False,default='')
    name = models.CharField(
        max_length=256,
        blank=False,
        )
    email = models.EmailField(
    max_length=70,
    blank=True)
    user_id = models.ForeignKey(User,
    null=True,
    blank=True)
