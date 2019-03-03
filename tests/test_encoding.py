import pytest


def test_any_characters__str_type():
    english_name = 'Wonder Chang'
    chinese_name = '張遠哲'

    assert isinstance(english_name, str)
    assert isinstance(chinese_name, str)

def test_byte_string_only_for_ASCII_literal_chars():
    english_name = b'Wonder Chang'

    # chinese_name = b'張遠哲'
    # SyntaxError: bytes can only contain ASCII literal characters.

    assert isinstance(english_name, bytes)

def test_unicode_string_convert_to_utf8_encoding():
    assert 'W' == '\u0057'
    assert 'W'.encode('utf-8') == b'W'

    assert '張' == '\u5f35'
    assert '張'.encode('utf-8') == b'\xe5\xbc\xb5'


# vi:et:ts=4:sw=4:cc=80
