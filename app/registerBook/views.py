from .forms import RegisterBookForm
from flask import render_template, flash
from . import regBook
from app.models import Book
from app import db


@regBook.route('/registerBook', methods=['GET', 'POST'])
def registerBook():
    form = RegisterBookForm()
    if form.validate_on_submit():
        book = Book()
        book.title = form.title.data
        book.author = form.author.data
        book.isbn = form.isbn.data
        book.publisher = form.publisher.data
        book.publication_date = form.publication_date.data
        book.genre = form.genre.data
        book.condition = form.condition.data
        db.session.add(book)
        db.session.commit()
        flash('Book registered successfully')
        return redirect('main.dashboard')
    return render_template('regBook.html', form=form)
