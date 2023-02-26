import pytest

from main import BooksCollector


@pytest.fixture()
def collector():
    collector = BooksCollector()

    return collector


@pytest.fixture()
def book():
    book = 'Над пропастью моржи'

    return book


@pytest.fixture
def collector_with_one_book(collector, book):
    collector.add_new_book(book)

    return collector
