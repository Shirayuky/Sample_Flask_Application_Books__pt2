from flask import Blueprint, render_template
from app.books.dao.books_dao import BooksDAO
from typing import List

PATH = './data/books.json'

books_blueprint = Blueprint('books_blueprint',
                            __name__,
                            template_folder='templates')
books_dao = BooksDAO(PATH)


@books_blueprint.route('/books')
def page_books_all():
    """Вьюшка для всех книг"""
    books: List[dict] = books_dao.get_all()
    return render_template('books_all.html', books=books)


@books_blueprint.route('/books/<int:pk>')
def page_book_by_pk(pk):
    """Вьюшка для всех книг"""
    book: dict = books_dao.get_by_pk(pk)
    return render_template('books_id.html', book=book, pk=pk)
