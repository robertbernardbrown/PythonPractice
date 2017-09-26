#import flask class from Flask module
from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps

#create the application object
app = Flask(__name__)

#would ideally be created by a random number generator
app.secret_key = "my precious" 

#login recquired decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

#use decorators to link functions to a URL
@app.route('/')
@login_required
def home():
		return render_template('index.html')

@app.route('/welcome')
def welcome():
		return render_template("welcome.html")

@app.route('/login', methods=['GET', 'POST'])			return redirect(url_for('home'))
	return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
	session.pop('logged_in', None)
	flash('You were just logged out')
	return redirect(url_for('welcome'))

#start the server with a run method
if __name__ == '__main__':
		app.run(debug=True)