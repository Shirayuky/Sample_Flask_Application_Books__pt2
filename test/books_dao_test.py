from app.books.dao.books_dao import BooksDAO
import pytest
from typing import List

keys_should_be = {'pk', 'title', 'pages'}


@pytest.fixture()
def books_dao():
    """Фикстура с экземпляром"""
    books_dao_instance = BooksDAO('./data/books.json')
    return books_dao_instance


class TestBooksDAO:
    """Класс для теста DAO Книг"""

    def test_get_all(self, books_dao):
        books = books_dao.get_all()
        assert type(books) == List[dict], "Загруженные данные из файла возвращаются не списком"
        assert len(books) > 0, "Список данных пуст"
        assert set(books[0].keys()) == keys_should_be, "Ключи списка книг не совпадают с ожидаемыми"

    def test_get_by_pk(self, books_dao):
        book = books_dao.get_by_pk(1)
        assert type(book) == dict, "Загруженные данные из файла возвращаются не словарем"
        assert book['pk'] == 1, "Возвращается неверная книга"
        assert set(book[0].keys()) == keys_should_be, "Ключи списка книг не совпадают с ожидаемыми"
