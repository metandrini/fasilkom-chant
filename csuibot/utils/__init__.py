from csuibot.utils import zodiac as z
from csuibot.utils import word as w


def lookup_zodiac(month, day):
    zodiacs = [
        z.Aries(),
        z.Leo(),
        z.Sagittarius(),
        z.Aquarius(),
        z.Gemini(),
        z.Cancer(),
        z.Scorpio(),
        z.Libra()
    ]

    for zodiac in zodiacs:
        if zodiac.date_includes(month, day):
            return zodiac.name
    else:
        return 'Unknown zodiac'


def lookup_chinese_zodiac(year):
    num_zodiacs = 12
    zodiacs = {
        0: 'rat',
        1: 'buffalo',
        4: 'dragon',
        5: 'snake',
        7: 'goat'
    }

    ix = (year - 4) % num_zodiacs

    try:
        return zodiacs[ix]
    except KeyError:
        return 'Unknown zodiac'


def lookup_word(action, word):
    searches = [
        w.Definition(word),
        w.Synonym(word),
        w.Antonym(word)
    ]

    for search in searches:
        if search.name == action:
            return search.lookup()
