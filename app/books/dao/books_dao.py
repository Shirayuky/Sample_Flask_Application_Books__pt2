import json
from typing import List


class BooksDAO:
    """Класс функциональности Книг"""

    def __init__(self, path):
        self.path = path

    def load_data(self) -> List[dict]:
        with open(self.path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data

    def get_all(self) -> List[dict]:
        books = self.load_data()
        return books

    def get_by_pk(self, pk) -> dict:
        books = self.load_data()
        for book in books:
            if book['pk'] == pk:
                return book
