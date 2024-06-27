from flask import Flask, render_template

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/about-us',methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/services',methods=['GET'])
def services():
    return render_template('services.html')

@app.route('/careers',methods=['GET'])
def careers():
    return render_template('careers.html')

@app.route('/contact',methods=['GET'])
def contact():
    return render_template('contact.html')

app.run(debug=True)