from .translator import Translator


def flask_methods(app, get_translations_file):
    @app.context_processor
    def trans(sentence):
        translator = Translator(get_translations_file())
        return translator.translate(sentence)
