# Translation Library with CSV

Translate a content from a CSV translation files.

## Example

### CSV files format

CSV files can have this format and should be UTF-8 encoded.

_my-translations-file.csv_:

```
TCI title,Titre ITC
"yes, or no","oui, ou non"
Welcome %(user)s!,Bienvenue %(user)s !
```

### Usage

```
from csvi18n import Translator

translator = Translator('my-translations-file.csv')
translator.translate('TCI title')  # => Titre ITC
```


### Run tests

```
python3 -m unittest
```

In a flask project:

*core.py*

```
from tcii18n.template import flask_methods

def get_translations_file():
    return 'path/to/my/file.csv'

flask_methods(app, get_translations_file)
```

*template.html*

```
<h1>{{ _("Sentence") }}</h1>
```

Where:

-get_translations_file() is a function that returns the appropriate translation file path
-flask_methods(app, get_translation_file) initializes the template processor
with app as your Flask instance and get_translation_file is the reference
 to the callable method.
