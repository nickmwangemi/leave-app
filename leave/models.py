from django.db import models

LEAVE_CHOICES = [
    ('NORMAL', 'Normal'),
    ('SICK_LEAVE', 'Sickleave'),
]

class LeaveRequest(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    type_of_leave = models.CharField(choices=LEAVE_CHOICES, default='NORMAL')