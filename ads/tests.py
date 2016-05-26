from django.test import TestCase

from . import models


class AdsTestCase(TestCase):
    def test_ads(self):
        for i in range(20):

            o = models.Ad(
                title="Puppy #{}".format(i + 1),
                description="lovely puppy, brown and happy",
                posted_by="Udi",
                contact_email="udi@10x.org.il",
                price=10 + i * 5,
                status= models.Ad.Status.NEW if i % 2 else models.Ad.Status.APPROVED
            )

            o.full_clean()
            o.save()


        self.assertEquals(models.Ad.objects.count(), 20)
