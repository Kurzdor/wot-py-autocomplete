
from constants import DEFAULT_LANGUAGE
from helpers import getClientLanguage

from ._constants import DEFAULT_UI_LANGUAGE, LANGUAGE_CODES, LANGUAGE_FILE_MASK
from .utils import parseLangFields, cacheResult

__all__ = ('l10n', )

_LANGUAGE = {}
_LANGUAGES = {}

for lang_code in LANGUAGE_CODES:
	vfs_path = LANGUAGE_FILE_MASK % lang_code
	vfs_data = parseLangFields(vfs_path)
	if vfs_data:
		_LANGUAGES[lang_code] = vfs_data

_CLIENT_LANGUAGE = getClientLanguage()
if _CLIENT_LANGUAGE in _LANGUAGES.keys():
	_LANGUAGE = _LANGUAGES[_CLIENT_LANGUAGE]
elif DEFAULT_LANGUAGE in _LANGUAGES.keys():
	_LANGUAGE = _LANGUAGES[DEFAULT_LANGUAGE]
else:
	_LANGUAGE = _LANGUAGES[DEFAULT_UI_LANGUAGE]

@cacheResult
def l10n(locale_key):
	'''returns localized value relative to locale_key'''
	if locale_key in _LANGUAGE:
		return _LANGUAGE[locale_key]
	elif locale_key in _LANGUAGES[DEFAULT_LANGUAGE]:
		return _LANGUAGES[DEFAULT_LANGUAGE][locale_key]
	elif locale_key in _LANGUAGES[DEFAULT_UI_LANGUAGE]:
		return _LANGUAGES[DEFAULT_UI_LANGUAGE][locale_key]
	return locale_key
