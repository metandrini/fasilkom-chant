import re

from . import app, bot
from .utils import lookup_zodiac, lookup_chinese_zodiac, lookup_word


@bot.message_handler(commands=['about'])
def help(message):
    app.logger.debug("'about' command detected")
    about_text = (
        'CSUIBot v0.0.1\n\n'
        'Dari Fasilkom, oleh Fasilkom, untuk Fasilkom!'
    )
    bot.reply_to(message, about_text)
    # print(about_text)


def _is_zodiac_command(message):
    regexp = r'/zodiac \d{4}\-\d{2}\-\d{2}'
    return re.match(regexp, message.text) is not None


def _is_shio_command(message):
    regexp = r'/shio \d{4}\-\d{2}\-\d{2}'
    return re.match(regexp, message.text) is not None


def _is_definition_command(message):
    regexp = r'/definition \S*'
    return re.match(regexp, message.text) is not None


def _is_synonym_command(message):
    regexp = r'/synonym \S*'
    return re.match(regexp, message.text) is not None


def _is_antonym_command(message):
    regexp = r'/antonym \S*'
    return re.match(regexp, message.text) is not None


@bot.message_handler(func=_is_zodiac_command)
def zodiac(message):
    app.logger.debug("'zodiac' command detected")
    _, date_str = message.text.split(' ')
    _, month, day = _parse_date(date_str)
    app.logger.debug('month = {}, day = {}'.format(month, day))
    bot.reply_to(message, lookup_zodiac(month, day))
    # print(lookup_zodiac(month, day))


@bot.message_handler(func=_is_shio_command)
def shio(message):
    app.logger.debug("'shio' command detected")
    _, date_str = message.text.split(' ')
    year, _, _ = _parse_date(date_str)
    app.logger.debug('year = {}'.format(year))
    bot.reply_to(message, lookup_chinese_zodiac(year))
    # print(lookup_chinese_zodiac(year))


def _parse_date(text):
    return tuple(map(int, text.split('-')))


@bot.message_handler(func=_is_definition_command)
def definition(message):
    app.logger.debug("'definition' command detected")
    action_str, word_str = _parse_word(message.text)
    app.logger.debug('action = {}, word = {}'.format(action_str, word_str))
    bot.reply_to(message, lookup_word(action_str, word_str))
    # print(lookup_word(action_str, word_str))


@bot.message_handler(func=_is_synonym_command)
def synonym(message):
    app.logger.debug("'synonym' command detected")
    action_str, word_str = _parse_word(message.text)
    app.logger.debug('action = {}, word = {}'.format(action_str, word_str))
    bot.reply_to(message, lookup_word(action_str, word_str))
    # print(lookup_word(action_str, word_str))


@bot.message_handler(func=_is_antonym_command)
def antonym(message):
    app.logger.debug("'antonym' command detected")
    action_str, word_str = _parse_word(message.text)
    app.logger.debug('action = {}, word = {}'.format(action_str, word_str))
    bot.reply_to(message, lookup_word(action_str, word_str))
    # print(lookup_word(action_str, word_str))


def _parse_word(text):  # return first word if input contains multiple words
    ret = text[1:].split(' ')
    return ret[:2] if len(ret) > 2 else ret
