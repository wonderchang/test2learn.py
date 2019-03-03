import pytest

import xml.etree.ElementTree as ET


@pytest.fixture
def bookstore():
    return ET.parse('tests/xml/data/bookstore.xml').getroot()

def test_namespace_findall(bookstore):
    ns = {'myns': 'http://my/ns'}
    titles = bookstore.findall('myns:book/myns:title', ns)

    assert [title.text for title in titles] == [
        'Harry Potter',
        'The Lord of the Rings',
    ]


# vi:et:ts=4:sw=4:cc=80
