from unittest import TestCase

def soma(a, b):
  return a + b

class TestMath(TestCase):

    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)