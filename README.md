1. test_add_new_book_add_existing_book проверяет, что нельзя добавить в словарь уже добавленную книгу
и что при попытке добавления существующей книги длина словаря не изменяется;
2. test_set_book_rating_set_5_existing_book проверяет, что метод set_book_rating выставляет рейтинг существующей 
в словаре книге;
3. test_set_book_rating_set_5_not_existing_book проверяет что книге, которая отсутствует в словаре, нельзя выставить
рейтинг и что при попытке выставления рейтинга такая книга не добавляется в словарь;
4. test_set_book_rating_set_0_and_11_existing_book проверяет, что существующим в словаре книгам нельзя проставить
рейтинг ниже 1 и больше 10, рейтинг книг в таком случае не изменится;
5. test_get_book_rating_get_existing_book_rating проверяет, что метод get_book_rating возвращает корректный
рейтинг книги;
6. test_get_books_with_specific_rating_get_books_with_rating_7 проверяет, что метод get_books_with_specific_rating
возвращает список книг с определенным рейтингом;
7. test_get_books_rating_get_dict_with_one_book проверяет, что метод get_books_rating возвращает словарь с 
ранее добавленной книгой и ее рейтингом;
8. test_add_book_in_favorites_add_one_book проверяет добавление существующей в словаре книги в избранное;
9. test_delete_book_from_favorites_delete_existing_book проверяет удаление ранее добавленной в избранное книги;
10. test_get_list_of_favorites_books_get_list_with_one_book проверяет, что метод get_list_of_favorites_books
возвращает список избранных книг.
