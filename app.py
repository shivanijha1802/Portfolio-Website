# app.py
# A Self Portfolio Website
# Author: Shivani Jha 
# Date: 2025-07-01
# Description: A professional personal portfolio website built using Flask, HTML, CSS, and Jinja2.

from flask import Flask, render_template, request

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Contact form page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Fetches data from the form
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print(f"Message from {name} ({email}): {message}")
        return render_template('thankuform.html', name=name)
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
