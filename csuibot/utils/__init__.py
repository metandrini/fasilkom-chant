from csuibot.utils import zodiac as z


def lookup_zodiac(month, day):
    zodiacs = [
        z.Aries(),
        z.Leo(),
        z.Sagittarius(),
        z.Aquarius(),
        z.Gemini()
    ]

    for zodiac in zodiacs:
        if zodiac.date_includes(month, day):
            return zodiac.name


def lookup_chinese_zodiac(year):
    num_zodiacs = 12
    zodiacs = [
        'rat',
        'other zodiac',
        'other zodiac',
        'other zodiac',
        'dragon'
    ]
    ix = (year - 4) % num_zodiacs

    try:
        return zodiacs[ix]
    except IndexError:
        return 'Unknown zodiac'
