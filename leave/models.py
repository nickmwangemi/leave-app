import datetime


import numpy as np
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import F, Q
from django.db.models.functions import Now
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


class LeaveRequest(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField(blank=False, validators=[validate_date_in_future])
    end_date = models.DateField(blank=False, validators=[validate_date_in_future])
    type_of_leave = models.CharField(
        max_length=255, choices=LEAVE_CHOICES, default="NORMAL", db_index=True
    )

    # Experimental feature at most. :)
    # Adds a constraint to check whether end_date comes after start_date
    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(start_date__lte=F("end_date")), name="correct_date"
            )
        ]

    def __str__(self):
        return f"{self.name} - {self.type_of_leave} leave request."

    def get_absolute_url(self):
        return reverse("leave:leave_request_detail", args=[str(self.id)])

    # @property
    # def count_workdays(self):
    #     return np.busday_count(self.start_date, self.end_date)

    @property
    def count_workdays(self):
        start_date = self.start_date
        end_date = self.end_date

        # Generate the dates that fall in between
        dates = set()
        for index in range((end_date - start_date).days):
            dates.add(start_date + datetime.timedelta(index + 1))

        # Sum the number of business days
        number_of_business_days = 0
        for day in dates:
            if day.weekday() < 5:
                number_of_business_days += 1
        return number_of_business_days


