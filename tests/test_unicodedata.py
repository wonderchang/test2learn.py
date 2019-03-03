from unicodedata import east_asian_width


def test_east_asian_width():
    # ea ; A         ; Ambiguous
    # ea ; F         ; Fullwidth
    # ea ; H         ; Halfwidth
    # ea ; N         ; Neutral
    # ea ; Na        ; Narrow
    # ea ; W         ; Wide

    # English letter and some common symbols with
    assert east_asian_width('W') == 'Na'
    assert east_asian_width('Ａ') == 'F'
    assert east_asian_width('％') == 'F'
    assert east_asian_width('　') == 'F'

    # Chinese, Japanese, Korean are belongs to "Wide"
    assert east_asian_width('張') == 'W'
    assert east_asian_width('ご') == 'W'
    assert east_asian_width('가') == 'W'

    # Latin
    assert east_asian_width('𐌌') == 'N'


# vi:et:ts=4:sw=4:cc=80
