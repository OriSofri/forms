from flask import Flask, render_template, url_for, redirect
from formStructs import RegistrationForm,LoginForm 
app = Flask(__name__)

app.config['SECRET_KEY']='7bcdf801ed94d527b1771a596b5c93b8'


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