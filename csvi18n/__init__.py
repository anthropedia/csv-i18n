import csv


_cached_translators = {}


class Translator:
    def __init__(self, filepath: str, use_cache: bool=True, fallback_path: str=None):
        self._cache_key = filepath
        self.use_cache = use_cache
        self.content = {}

        if fallback_path:
            reader = open(fallback_path, 'r')
            self.content.update(dict(row for row in csv.reader(reader) if len(row)))
            reader.close()

        reader = open(filepath, 'r')
        self.content.update(dict(row for row in csv.reader(reader) if len(row)))
        reader.close()

        if self.use_cache and self._cache_key not in _cached_translators.keys():
            _cached_translators[self._cache_key] = self.content


    def get_translations(self) -> tuple:
        if self.use_cache:
            return _cached_translators[self._cache_key]
        else:
            return self.content

    def translate(self, sentence: str, **kwargs) -> str:
        translation = dict(self.get_translations()).get(sentence)
        if not translation:
            return sentence
        for key, value in kwargs.items():
            translation = translation % {key: value}
        return translation
