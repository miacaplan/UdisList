from django.test import TestCase

from . import models


class AdsTestCase(TestCase):
    def test_ads(self):
        for i in range(20):
            o = models.Ad()
            o.title = "Puppy #{}".format(i + 1)
            o.description = "lovely puppy, brown and happy"
            o.posted_by = "Udi"
            o.contact_email = "udi@10x.org.il"
            o.price = 10 + i * 5
            o.full_clean()
            o.save()

        self.assertEquals(models.Ad.objects.count(), 20)
