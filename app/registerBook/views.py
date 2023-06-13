from .forms import RegisterBookForm
from flask import render_template
from . import regBook


@regBook.route('/registerBook', methods=['GET', 'POST'])
def registerBook():
    form = RegisterBookForm()
    return render_template('regBook.html', form=form)
