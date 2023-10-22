from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo
from flask_login import UserMixin, login_user, logout_user, login_required, LoginManager, before_first_request
import os

app = Flask(__name__)
app.secret_key = os.urandom(100000)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_manager.db'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

@app.route('/')
def index():
    return "hello world"

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(max=15)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(max=80)])
    password = PasswordField('Password', validators=[DataRequired()])

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data 
        password = form.password.data
        print(username, password)
        user = User(username=username, password=password)
        print(user)
        db.session.add(user)
        db.session.commit()
        flash("registration successful you can now login")
        return redirect(url_for("login"))
    return render_template('register.html', form=form)

@app.route('/login', methods = ['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash("login successful")
            return redirect(url_for('index'))
        else:
            flash("login failed. please check your username and password")
            
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def Logout():
    logout_user()
    flash("you have been logged out")
    return redirect(url_for('index'))

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)