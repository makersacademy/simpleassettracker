from django.test import TestCase

class FirstTest(TestCase):
    def test_something_that_will_pass(self):
        self.assertFalse(False)

    def test_something_that_will_fail(self):
        self.assertTrue(False)