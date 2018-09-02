from unittest import TestCase
from app import is_palindrome
#import app

#print(dir(app))

class TestPalindrome(TestCase):
    def setUp(self):
        self.words = ["silas", "salas", "a", "aba", "acb", "aaa"]
        self.answers = [False, False, True, True, False, True]
    def tearDown(self):
        self.words = []
        self.answers = []
    def test_one_letter(self):
        self.assertEqual(is_palindrome(self.words[0]), self.answers[0])
    def test_false(self):
        self.assertEqual(is_palindrome("sal"), False)
    def test_true(self):
        self.assertEqual(is_palindrome("sonos"), True)
    def test_mixed_case(self):
        self.assertEqual(is_palindrome("Madam"), True)
