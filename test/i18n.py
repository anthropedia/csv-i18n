from unittest import TestCase
from csvi18n import Translator


class I18nTest(TestCase):
    def setUp(self):
        self.translator = Translator('test/fixtures.fr.csv')
        self.trans = self.translator.translate
        translator = Translator('test/fixtures.it.csv')
        self.trans_it = translator.translate

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

    def test_display_unknown_message(self):
        self.assertEqual(self.trans('Unknown message'), 'Unknown message')

    def test_caching_documents(self):
        self.assertEqual(self.translator._cache['TCI title'], 'Titre ITC')
        translator = Translator('test/fixtures.fr.csv', cache=False)
        self.assertDeepEqual(self.translator._cache, {})
