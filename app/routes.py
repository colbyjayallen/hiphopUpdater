from flask import render_template, flash, redirect, url_for
from app import app
import os
from app.forms import UnsubForm, SignUpForm
from app.models import User, Rapper, delete_user, import_user


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        rappers = form.rappers.data
        email = form.email.data
        for r in rappers:
            import_user(email, r.id)
        return redirect(url_for('signupsuccess'))
    return render_template('signup.html', title='Sign Up', form=form)


@app.route('/unsub', methods=['GET', 'POST'])
def unsub():
    form = UnsubForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            flash('That email is not contained in our records.')
            return redirect(url_for('unsub'))
        delete_user(form.email.data)
        return redirect(url_for('unsubsuccess'))
    return render_template('unsub.html', title='Unsubscribe', form=form)


@app.route('/unsubsuccess')
def unsubsuccess():
    return render_template('unsubsuccess.html', title='Success!')


@app.route('/signupsuccess')
def signupsuccess():
    return render_template('signupsuccess.html', title='Success!')
