import pytest


class TestBooksCollector:


    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_rating()) == 2


    def test_add_new_book_add_existing_book(self, collector_with_one_book, book):
        collector_with_one_book.add_new_book(book)

        assert len(collector_with_one_book.get_books_rating()) == 1


    def test_set_book_rating_set_5_existing_book(self, collector_with_one_book, book):
        collector_with_one_book.set_book_rating(book, 5)

        assert collector_with_one_book.get_book_rating(book) == 5


    def test_set_book_rating_set_5_not_existing_book(self, collector, book):
        collector.set_book_rating(book, 5)

        assert not collector.get_book_rating(book) == 5


    @pytest.mark.parametrize('name, rating', [['Горе о туман', 0], ['Обком звонит в колокол', 11]])
    def test_set_book_rating_set_0_and_11_existing_book(self, name, rating, collector):

        collector.add_new_book(name)
        collector.set_book_rating(name, rating)

        assert not collector.get_book_rating(name) == rating


    def test_get_book_rating_get_existing_book_rating(self, collector_with_one_book, book):

        assert collector_with_one_book.get_book_rating(book) == 1


    def test_get_books_with_specific_rating_get_books_with_rating_7(self, collector_with_one_book, book):
        collector_with_one_book.set_book_rating(book, 7)

        assert collector_with_one_book.get_books_with_specific_rating(7) == [book]


    def test_get_books_rating_get_dict_with_one_book(self, collector_with_one_book, book):
        collector_with_one_book.set_book_rating(book, 2)

        books_rating = collector_with_one_book.get_books_rating()

        assert books_rating[book] == 2 and len(books_rating) == 1


    def test_add_book_in_favorites_add_one_book(self, collector_with_one_book, book):
        collector_with_one_book.add_book_in_favorites(book)

        assert collector_with_one_book.favorites == [book]


    def test_delete_book_from_favorites_delete_existing_book(self, collector_with_one_book, book):
        collector_with_one_book.add_book_in_favorites(book)
        collector_with_one_book.delete_book_from_favorites(book)

        assert collector_with_one_book.favorites == []


    def test_get_list_of_favorites_books_get_list_with_one_book(self, collector_with_one_book, book):
        collector_with_one_book.add_book_in_favorites(book)

        assert collector_with_one_book.get_list_of_favorites_books() == [book]
