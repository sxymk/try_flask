from flask import Blueprint,render_template

#url_prefix: 127.0.0.1:5000/book
bp = Blueprint("book",__name__,url_prefix="/book")

@bp.route('/list')
def book_list():
    return render_template("book_list.html")