from unittest import TestCase
from tcii18n import trans


class I18nTest(TestCase):
    def setUp(self):
        self.trans = trans._
        self.trans_it = None

    def test_translate(self):
        self.assertEqual(self.trans('TCI title'), 'Titre ITC')
        self.assertEqual(self.trans('yes, or no'), 'oui, ou non')

    def test_substitute(self):
        self.assertEqual(self.trans('Welcome %(user)s!', user='John'),
                         'Bienvenue John !')

    def test_switch_language(self):
        self.assertEqual(self.trans_it('TCI title'), 'ITC titolo')
        self.assertEqual(self.trans_it('Welcome %(user)s!', user='John'),
                         'Benvenuto John!')
