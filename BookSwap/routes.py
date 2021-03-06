from BookSwap import app, db
from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, logout_user, login_required, current_user
from BookSwap.models import Users, Book
from BookSwap.forms import LoginForm, RegisterForm, AddBooksSearch, AddBooksForm
import requests
from urllib import parse


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/login', methods=['POST', 'GET'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = Users.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Welcome back, {attempted_user.name}!', category='success')
            return redirect(request.args.get('next') or url_for('home_page'))
        else:
            flash('Username or password is not correct! Please try again', category='error')

    return render_template('login.html', form=form)


@app.route('/logout')
def logout_page():
    logout_user()
    flash('We\'ll miss you, come back soon!', category='info')
    return redirect(url_for('home_page'))


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = Users(name=form.name.data,
                              username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f'Account created successfully! You are now logged in as {user_to_create.name}', category='success')
        return redirect(url_for('home_page'))
    if form.errors != {}:  # If there are errors from the validations
        for err_msg in form.errors.values():
            flash(f'{err_msg[0]}', category='error')

    return render_template('register.html', form=form)


@app.route('/add-books', methods=['GET', 'POST'])
@login_required
def add_books():
    search_form = AddBooksSearch()
    add_form = AddBooksForm()
    search_url = 'https://www.googleapis.com/books/v1/volumes?'
    search_data = []

    if request.method == 'POST':
        if 'search_book' in request.form:
            if request.form.get('author') == '':
                search_params = {
                    'q': f'intitle:{request.form.get("title")}',
                    'printType': 'books',
                    'langRestrict': 'en',
                    'maxResults': '30'
                }
            elif request.form.get('title') == '':
                search_params = {
                    'q': f'inauthor:{request.form.get("author")}',
                    'printType': 'books',
                    'langRestrict': 'en',
                    'maxResults': '30'
                }
            else:
                search_params = {
                    'q': f'inauthor:{request.form.get("author")}+intitle:{request.form.get("title")}',
                    'printType': 'books',
                    'langRestrict': 'en',
                    'projection': 'lite',
                    'maxResults': '30'
                }

            r = requests.get(search_url, params=parse.urlencode(search_params))

            results = r.json().get('items')

            if results:
                for result in results:
                    entry = {
                        'volume_id': result['id'],
                        'title': result['volumeInfo'].get('title'),
                        'authors': result['volumeInfo'].get('authors'),
                        'subtitle': result['volumeInfo'].get('subtitle'),
                        'description': result['volumeInfo'].get('description'),
                        'categories': result['volumeInfo'].get('categories'),
                        'image': result['volumeInfo'].get('imageLinks', {}).get('thumbnail')
                    }

                    search_data.append(entry)

            else:
                flash('No results found. Please try another search.', category='error')

    if 'book-author' in request.form:
        new_book = Book(volume_id=request.form.get('book-volume'),
                        title=request.form.get('book-title'),
                        author=request.form.get('book-author'),
                        subtitle=request.form.get('book-subtitle'),
                        description=request.form.get('book-description'),
                        categories=request.form.get('book-categories'),
                        image=request.form.get('book-image'),
                        owner=current_user.id)

        db.session.add(new_book)
        db.session.commit()

        flash(f'{request.form.get("book-title")} added!', category='success')

    return render_template('add-books.html', search_form=search_form, add_form=add_form, search_data=search_data)

