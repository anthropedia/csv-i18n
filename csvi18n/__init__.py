import csv


_cached_translators = {}


class Translator:
    def __init__(self, filename: str, use_cache: bool=True):
        self._cache_key = filename
        self._translator = _chached_translators if use_cache else {}
        reader = open(filename, 'r')
        self.content = tuple(row for row in csv.reader(reader) if len(row))
        reader.close()
        if self._cache and self._cache_key not in _translators.keys():
            _translators[self._cache_key] = self.content

    def get_translations(self) -> tuple:
        if self.use_cache:
            return _translators[self._cache_key]
        else:
            return self.content

    def translate(self, sentence: str, **kwargs) -> str:
        translation = dict(self.get_translations()).get(sentence)
        if not translation:
            return sentence
        for key, value in kwargs.items():
            translation = translation % {key: value}
        return translation