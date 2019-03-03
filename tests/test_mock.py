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




# vi:et:ts=4:sw=4:cc=80
