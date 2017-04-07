from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from django.core.urlresolvers import reverse

class Event(models.Model):
    TIME_CHOICES=(('1','9.00-10.00'),
    ('2','10.00-11.00'),
    ('3','11.00-12.00'))
    start_date = models.DateField(
      blank=False)
    start_time = MultiSelectField(choices=TIME_CHOICES,
    max_choices=3,
    blank=False,
    default='')
    end_date = models.DateField(
      blank=False)
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
    def selected_choices(self):
        choice = []
        for el in self.start_time:
            for key,val in self.TIME_CHOICES:
                if el==key:
                    choice.append(val)
        return choice
    def get_absolute_url(self):
        return reverse('start_page')
