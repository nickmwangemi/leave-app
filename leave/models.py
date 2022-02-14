import datetime

from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse

LEAVE_CHOICES = [
    ("NORMAL", "Normal"),
    ("SICK_LEAVE", "Sick leave"),
]


def validate_date_in_future(date):
    now = datetime.date.today()
    if date < now:
        raise ValidationError("Date must be in the future.")
    return date


def validate_end_date_comes_after_start_date():
    pass


class LeaveRequest(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField(blank=False, validators=[validate_date_in_future])
    end_date = models.DateField(blank=False, validators=[validate_date_in_future])
    type_of_leave = models.CharField(
        max_length=255, choices=LEAVE_CHOICES, default="NORMAL", db_index=True
    )

    def __str__(self):
        return f"{self.name} - {self.type_of_leave} leave request."

    def get_absolute_url(self):
        return reverse("leave:leave_request_detail", args=[str(self.id)])
