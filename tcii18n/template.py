from .translator import Translator

_cached_translators = {}


def flask_methods(app, get_translations_file):
    @app.context_processor
    def utility_processor():
        def trans(sentence):
            filename = get_translations_file()
            if filename not in _cached_translators:
                _cached_translators[filename] = Translator(filename)
            return _cached_translators[filename].translate(sentence)
        return dict(trans=trans, _=trans)
