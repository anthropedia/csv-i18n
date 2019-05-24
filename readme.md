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
