from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from formStructs import RegistrationForm,LoginForm 
app = Flask(__name__)

app.config['SECRET_KEY']='7bcdf801ed94d527b1771a596b5c93b8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

#creating the DataBase structure
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False )
    email = db.Column(db.String, unique=True, nullable=False )
    password = db.Column(db.String, unique=True, nullable=False )
    posts= db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title  = db.Column(db.String, nullable=False )
    content = db.Column(db.Text, nullable=False )
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}')"

@app.route('/')
@app.route('/Home')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form= form)


@app.route('/login')
def login():
    form= LoginForm()
    return render_template('login,html', title='Login', form= form)

#allowing python to run the file  
if __name__ == '__main__':
    app.run(debug=True)