from hashid_field import HashidAutoField

from django.db import models
from django.utils import timezone


class Event(models.Model):
    impression = 'impression'
    engagement = 'engagement'
    STATUS_TYPE_CHOICES = (
        (impression, 'impression'),
        (engagement, 'engagement'),
    )

    id = HashidAutoField(primary_key=True)
    created_datetime = models.DateTimeField(auto_now_add=timezone.now)
    type = models.CharField(max_length=50, choices=STATUS_TYPE_CHOICES, default=impression)
    domain = models.CharField(max_length=250)
    parameter = models.CharField(max_length=250)



