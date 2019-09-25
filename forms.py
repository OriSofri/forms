from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/Home')
def home():
    return render_template('home.html')

#allowing python to run the file  
if __name__ == '__main__':
    app.run(debug=True)