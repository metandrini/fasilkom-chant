from unittest.mock import Mock

from csuibot.handlers import help, zodiac, shio, definition, synonym, antonym


def test_help(mocker):
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mock_message = Mock()
    help(mock_message)

    args, _ = mocked_reply_to.call_args
    expected_text = (
        'CSUIBot v0.0.1\n\n'
        'Dari Fasilkom, oleh Fasilkom, untuk Fasilkom!'
    )
    assert args[1] == expected_text


def test_zodiac(mocker):
    fake_zodiac = 'foo bar'
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch('csuibot.handlers.lookup_zodiac', return_value=fake_zodiac)
    mock_message = Mock(text='/zodiac 2015-05-05')
    zodiac(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == fake_zodiac


def test_shio(mocker):
    fake_shio = 'foo bar'
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch('csuibot.handlers.lookup_chinese_zodiac', return_value=fake_shio)
    mock_message = Mock(text='/shio 2015-05-05')
    shio(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == fake_shio


def test_definition(mocker):
    fake_definition = 'foo bar'
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch('csuibot.handlers.lookup_word', return_value=fake_definition)
    mock_message = Mock(text='/definition school')
    definition(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == fake_definition


def test_synonym(mocker):
    fake_synonym = 'foo bar'
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch('csuibot.handlers.lookup_word', return_value=fake_synonym)
    mock_message = Mock(text='/synonym sleepy')
    synonym(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == fake_synonym


def test_antonym(mocker):
    fake_antonym = 'foo bar'
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch('csuibot.handlers.lookup_word', return_value=fake_antonym)
    mock_message = Mock(text='/antonym sleepy')
    antonym(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == fake_antonym
