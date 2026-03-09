import locale
from pathlib import Path

import pytest


STR_ENCODE_DATA_DIR = Path(__file__).parent / "data" / "str_encode"

def test_string_are_str_type():
    english_name = 'Wonder Chang'
    chinese_name = '張遠哲'

    assert isinstance(english_name, str)
    assert isinstance(chinese_name, str)

def test_byte_string_only_for_ascii_chars():
    english_name = b'Wonder Chang'

    # chinese_name = b'張遠哲'
    # SyntaxError: bytes can only contain ASCII literal characters.

    assert isinstance(english_name, bytes)

def test_unicode_string_to_utf8_byte():
    assert 'W' == '\u0057'
    assert 'W'.encode('utf-8') == b'W'

    assert '張' == '\u5f35'
    assert '張'.encode('utf-8') == b'\xe5\xbc\xb5'

def test_most_locale_encoding_is_utf8_by_default():
    assert locale.getencoding() == 'UTF-8'

@pytest.mark.parametrize("filename,encoding,expected", [
    ("utf8_sample.txt", "utf8", "繁體中文。"),
    ("big5_sample.txt", "big5", "big5繁體中文。"),
    ("eucjp_sample.txt", "euc_jp", "eucjp日本語です。"),
])
def test_readfile_with_encoding(filename, encoding, expected):
    filepath = STR_ENCODE_DATA_DIR / filename
    with open(filepath, encoding=encoding) as fp:
        data = fp.read()

    assert isinstance(data, str)
    assert expected in data

def test_readfile_with_wrong_encoding():
    filepath = STR_ENCODE_DATA_DIR / 'utf8_sample.txt'
    with pytest.raises(UnicodeDecodeError) as err:
        with open(filepath, encoding='big5') as fp:
            data = fp.read()

    assert "'big5' codec can't decode byte 0x81 in position 2: illegal multibyte sequence" == str(err.value)

@pytest.mark.parametrize("filename,encoding,expected", [
    ("utf8_sample.txt", "utf8", "繁體中文。"),
    ("big5_sample.txt", "big5", "big5繁體中文。"),
    ("eucjp_sample.txt", "euc_jp", "eucjp日本語です。"),
])
def test_readfile_as_bytes_then_decode(filename, encoding, expected):
    filepath = STR_ENCODE_DATA_DIR / filename
    with open(filepath, 'rb') as fp:
        data = fp.read()

    assert isinstance(data, bytes)
    assert expected in data.decode(encoding)


# vi:et:ts=4:sw=4:cc=80
