import gettext





es = gettext.translation('guess',
                         localedir='locale',
                         languages=['es'],
                         fallback=True)
es.install()
_ = es.gettext
print(_('Hello World'))

