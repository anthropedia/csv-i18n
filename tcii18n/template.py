from .translator import Translator


def flask_methods(app, get_translations_file):
    @app.context_processor
    def utility_processor():
        def trans(sentence):
            return Translator(get_translations_file).translate(sentence)
        return dict(trans=trans)
