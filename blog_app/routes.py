from . import app
from flask import render_template, redirect, url_for, flash
from .forms import LoginForm

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login for {form.username.data } is successful')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/')
@app.route('/index')
def index():
    return render_template('snippets.html', title="Home")