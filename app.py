import os
print("Templates folder contents:", os.listdir(os.path.join(os.getcwd(), "templates")))

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    print("Home page loaded")
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/project')
def project():
    return render_template('project.html')

if __name__ == '__main__':
    app.run(debug=True)
