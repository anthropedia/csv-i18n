from unittest import TestCase
from tcii18n import trans


class I18nTest(TestCase):
    def setUp(self):
        self.trans = trans._

    def test_translate(self):
        self.assertEqual(self.trans('TCI title'), 'Titre ITC')
        self.assertEqual(self.trans('yes, or no'), 'oui, ou non')

    def test_substitute(self):
        self.assertEqual(self.trans('Welcome %(user)s!', user='John'),
                         'Bienvenue John !')
