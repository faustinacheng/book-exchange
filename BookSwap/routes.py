from flask_wtf import form
from BookSwap import app, login_manager, db
from flask import render_template, url_for, flash, redirect
from flask_login import login_user, logout_user
from BookSwap.models import User
from BookSwap.forms import LoginForm, RegisterForm


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/login', methods=['POST', 'GET'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(email_address=form.email_address.data).first()
        if attempted_user and attempted_user.check_password(attempted_password = form.password.data):
            login_user(attempted_user)
            flash(f'You are Successfully logged in as { attempted_user.name }')
            return redirect(url_for('home_page'))
        else: 
            flash('Username and Password don\'t match! Please try again', category='')

    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash('You have been Logged Out!', category='')
    return redirect(url_for('home_page'))

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(name=form.name.data, 
                                email_address=form.email_address.data, 
                                password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f"Account created successfully! You are now logged in as {user_to_create.name}", category='')
        return redirect(url_for('home_page'))
    if form.errors != {}: #If there are errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='')

    return render_template('register.html', form=form)