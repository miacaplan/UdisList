from django.test import TestCase


class SimpleTestCase(TestCase):
    def test_multiply_ok(self):
        url = "/x/4/5/"
        expected = "4 * 5 = 20"

        resp = self.client.get(url)

        self.assertContains(resp, expected)

    def test_multiply_bad(self):
        url = "/x/kuku/5/"
        expected = "bad request"

        resp = self.client.get(url)

        self.assertContains(resp, expected, status_code=400)

    def test_404(self):
        url = "/blahblahblah/"
        resp = self.client.get(url)
        self.assertEquals(resp.status_code, 404)

