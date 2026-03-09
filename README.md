# test2learn.py

A collection of executable Python tests for learning and exploring Python standard library behaviors. Each test file focuses on a specific topic and documents how Python really works — useful for developers who prefer reading runnable code over prose.

## Topics Covered

| Module / Topic | File | What You'll Learn |
|---|---|---|
| Collections | `tests/test_collection.py` | `tuple` immutability, `namedtuple` usage and `_replace` |
| Copy | `tests/test_copy.py` | Reference binding, shallow vs deep copy for dicts, lists, and objects; `deepcopy` memo behavior |
| Decorator | `tests/test_decorator.py` | Decorator stacking order and how it affects output |
| Generator | `tests/test_generator.py` | Generator functions with `yield`, lazy evaluation |
| Iterable | `tests/test_iterable.py` | Custom iterable classes (`__iter__`/`__next__`), finite vs infinite iterables |
| itertools | `tests/test_itertools.py` | `itertools.product` for Cartesian products |
| List Comprehension | `tests/test_list_comprehension.py` | Generator expressions, performance vs `for`-loop with `append` |
| Mock | `tests/test_mock.py` | `Mock` vs `MagicMock`, `mock_calls`, `assert_has_calls` |
| Pickle | `tests/test_pickle.py` | Serializing and deserializing Python objects to/from files |
| String Encoding | `tests/test_str_encode.py` | `str` vs `bytes`, UTF-8/Big5/EUC-JP file reading, encoding errors |
| Unicode Data | `tests/test_unicodedata.py` | East Asian width categories (Narrow, Wide, Fullwidth, etc.) |
| XML / ElementTree | `tests/xml/test_etree.py` | Parsing XML with namespaces using `xml.etree.ElementTree` |

## Requirements

- Python >= 3.12
- [uv](https://docs.astral.sh/uv/) (package manager)

## Quickstart

```bash
# Install dependencies
make sync

# Run all tests (excluding performance tests)
make test

# Run a specific test file
make test TEST=tests/test_copy.py

# Run performance tests
make test-perf

# Run all tests including performance tests
make test-all

# Clean generated files
make clean
```

## Philosophy

Tests in this repo serve as **living documentation**. Instead of explaining Python in paragraphs, each test case asserts exactly what happens — making it easy to verify understanding interactively:

```python
# From test_copy.py — shallow copy shares nested references
clone['cards'].append('ghi789')
assert (clone['cards'] is data['cards']) is True   # shallow copy!

# Deep copy creates fully independent clones
clone = copy.deepcopy(data)
assert (clone['cards'] is data['cards']) is False  # deep copy!
```

Performance tests (marked `@pytest.mark.perf`) are separated so the regular test suite stays fast. Run them explicitly when you want to compare approaches like list comprehension vs `for`-loop.

## License

MIT
