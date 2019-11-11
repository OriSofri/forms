from flask import Flask, render_template, url_for 
from formStructs import *
app = Flask(__name__)

@app.route('/')
@app.route('/Home')
def home():
    return render_template('home.html')

@app.route('/Registration')
def registration():
    return ''

    
@app.route('/Login')
def login():
    return ''

#allowing python to run the file  
if __name__ == '__main__':
    app.run(debug=True)