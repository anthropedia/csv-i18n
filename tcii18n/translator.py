import csv


_translators = {}


class Translator:
    def __init__(self, filename, cache=True):
        self._cache_key = filename
        self._cache = cache
        reader = open(filename, 'r')
        self.content = tuple(csv.reader(reader))
        reader.close()
        if self._cache and self._cache_key not in _translators.keys():
            _translators[self._cache_key] = self.content

    def get_translations(self):
        if self._cache:
            return _translators[self._cache_key]
        else:
            return self.content

    def translate(self, sentence, **kwargs):
        translation = dict(self.get_translations()).get(sentence)
        if not translation:
            return sentence
        for key, value in kwargs.items():
            translation = translation % {key: value}
        return translation
