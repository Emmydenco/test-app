# let's import the flask
from flask import Flask, render_template, request,redirect,url_for
import os # importing operating system module

app = Flask(__name__)

@app.route('/') # this decorator create the home route
def home ():
    # return '<h1>Welcome to Denis World! \n Today is the day the lord has made, I will rejoice and be glad in him...</h1>'
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30 Days Of Python Programming'
    return render_template('home.html', techs=techs, name = name, title = 'Home')


@app.route('/about')
def about():
    # return '<h1>About us</h1>'
    name = '30 Days Of Python Programming'
    return render_template('about.html', name = name, title = 'About Us')

@app.route('/contact_info')
def contact():
    return ' <h2>Call/WhatsApp us at 08069833243</h2>'

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/post', methods= ['GET','POST'])
def post():
    name = 'Text Analyzer'
    if request.method == 'GET':
         return render_template('post.html', name = name, title = name)
    if request.method =='POST':
        content = request.form['content']
        print(content)
        return redirect(url_for('result'))

if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    # port = int(os.environ.get("PORT", 5000))
    port = 5000
    app.run(debug=True, host='0.0.0.0', port=port)
