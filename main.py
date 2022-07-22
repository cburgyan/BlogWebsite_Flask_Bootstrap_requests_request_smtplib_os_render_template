from flask import Flask, render_template
import requests


app = Flask(__name__)


URL = 'https://api.npoint.io/ec84679d2403beee8160'
response_json = requests.get(url=URL).json()
# print(response_json)


@app.route('/')
def home_page():
    return render_template('index.html', blog_posts=response_json)


@app.route('/about.html')
def about_page():
    return render_template('about.html')


@app.route('/contact.html')
def contact_page():
    return render_template('contact.html')


@app.route('/post.html')
def post_page():
    return render_template('post.html')


if __name__ == "__main__":
    app.run(debug=True)


