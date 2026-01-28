from unittest import mock

import pytest


def test_mock_and_magic_mock():
    mock1 = mock.Mock()
    mock2 = mock.MagicMock()

    with pytest.raises(TypeError) as err:
        list(mock1)
        len(mock1)
        dict(mock1)

    assert list(mock2) == []
    assert len(mock2) == 0
    assert dict(mock2) == {}

def test_assert_has_calls_and_mock_calls():
    obj = mock.MagicMock()
    obj.one()
    obj.two()
    obj.three()
    obj.four()

    # https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.mock_calls
    assert obj.mock_calls == [
        mock.call.one(), mock.call.two(), mock.call.three(), mock.call.four(),
    ]

    # https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_has_calls
    obj.assert_has_calls([
        mock.call.one(), mock.call.two(), mock.call.three(),
    ])
    with pytest.raises(AssertionError) as err:
        obj.assert_has_calls([mock.call.one(), mock.call.three()])
    assert str(err.value) == (
        'Calls not found.\n'
        'Expected: [call.one(), call.three()]\n'
        '  Actual: [call.one(), call.two(), call.three(), call.four()]'
    )



# vi:et:ts=4:sw=4:cc=80
