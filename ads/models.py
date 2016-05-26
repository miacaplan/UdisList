from django.db import models


class Ad(models.Model):
    posted_at = models.DateTimeField(auto_now_add=True)

    title = models.CharField(max_length=200)
    description = models.TextField()

    posted_by = models.CharField(max_length=200)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=30,
                                     null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)
