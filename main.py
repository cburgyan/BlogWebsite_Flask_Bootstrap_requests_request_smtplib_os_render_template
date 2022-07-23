from flask import Flask, render_template, request
import requests


app = Flask(__name__)


URL = 'https://api.npoint.io/98b105151915c6944658'
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


@app.route('/form-entry', methods=['POST', 'GET'])
def receive_data():
    print(request.form['username'])
    print(request.form['email'])
    print(request.form['phone'])
    print(request.form['message'])
    return f'<h1>Successfully Sent Your Message</h1>'


@app.route('/post/<blog_id>')
def post_page(blog_id):
    page_post = {}
    for post in response_json:
        print(post)
        if post['id'] == int(blog_id):
            page_post = post
            break

    return render_template('post.html', page_post=page_post)


if __name__ == "__main__":
    app.run(debug=True)


