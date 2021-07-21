from BookSwap import app, login_manager, db
from flask import render_template, url_for, flash, redirect
from flask_login import login_user, logout_user
from BookSwap.models import User
from BookSwap.forms import RegisterForm


@app.route('/')
@app.route('/home')
@login_manager.user_loader
def home_page():
    return render_template('home.html')

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
        flash(f"Account created successfully! You are now logged in as {user_to_create.username}", category='success')
        return redirect(url_for('home_page'))
    if form.errors != {}: #If there are errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('register.html', form=form)