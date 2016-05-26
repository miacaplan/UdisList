from django.db import models


class Ad(models.Model):
    class Status:
        NEW = 1
        APPROVED = 2
        UNAPPROVED = 100

        choices = (
            (NEW, 'New'),
            (APPROVED, 'Approved'),
            (UNAPPROVED, 'Unapproved'),
        )

    posted_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=Status.choices, default=Status.NEW)

    title = models.CharField(max_length=200)
    description = models.TextField()

    posted_by = models.CharField(max_length=200)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=30,
                                     null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return "#{} ({})".format(self.id or "?", self.title)
