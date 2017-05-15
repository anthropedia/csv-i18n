# TCI Translation Library

Translate the TCI interface from CSV translation files.

## Example

TCI-i18n provides translation from CSV files.

### CSV files format

CSV files can have this format and should be UTF-8 encoded

```
TCI title,Titre ITC
"yes, or no","oui, ou non"
Welcome %(user)s!,Bienvenue %(user)s !
```

### Usage

```
from tcii18n import Translator

translator = Translator('my_file.csv')
translator.translate('My string')
```
