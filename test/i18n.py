from unittest import TestCase


class I18nTest(TestCase):
    def setUp(self):
        self.trans = None

    def test_translate(self):
        self.assertEqual(self.trans('TCI Title'), 'Titre ITC')
        self.assertEqual(self.trans('yes, or no'), 'oui, ou non')

    def test_substitute(self):
        self.assertEqual(self.trans('Welcome %(user)!', user='John'),
                         'Bienvenue John !')
