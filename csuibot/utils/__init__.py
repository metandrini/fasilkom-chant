from csuibot.utils import zodiac as z


def lookup_zodiac(month, day):
    zodiacs = [
        z.Aries(),
        z.Aquarius()
    ]

    for zodiac in zodiacs:
        if zodiac.date_includes(month, day):
            return zodiac.name


def lookup_chinese_zodiac(year):
    num_zodiacs = 12
    zodiacs = [
        'rat'
    ]
    ix = (year - 4) % num_zodiacs

    try:
        return zodiacs[ix]
    except IndexError:
        return 'Unknown zodiac'
