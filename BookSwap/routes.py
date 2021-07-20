from BookSwap import app, login_manager
from flask import render_template, url_for

@app.route('/')
@app.route('/home')
@login_manager.user_loader
def home_page():
    return render_template('home.html')