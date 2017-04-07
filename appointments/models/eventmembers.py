from django.db import models

class EventMember(models.Model):
    fullname = models.CharField(
        max_length=256,
        blank=False,
        )
    email = models.EmailField(
    max_length=70,
    blank=True)
    choosed_date = models.DateField(
      blank=False)
    choosed_time = models.TimeField(
      blank=False)
