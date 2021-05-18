import locale
import datetime

# for each locale
for loc in locale.windows_locale.values():
    try:
        # set Python to use the locale
        locale.setlocale(locale.LC_ALL, loc)
        # create a timestamp
        now = datetime.datetime.now()
        format = "%A, %d %b %Y %H:%M:%S %Z"
        now = now.strftime(format)
        # print the locale and the timestamp in that locale
        print(loc, now)
    except:
        # if the locale code doesn't work, just skip
        pass