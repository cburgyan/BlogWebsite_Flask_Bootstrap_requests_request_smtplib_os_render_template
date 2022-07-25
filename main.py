from flask import Flask, render_template, request
import requests
import os
import smtplib


app = Flask(__name__)
MY_EMAIL = os.environ.get('EMAIL')
MY_PASSWORD = os.environ.get('PASSWORD')


URL = 'https://api.npoint.io/98b105151915c6944658'
response_json = requests.get(url=URL).json()


@app.route('/')
def home_page():
    return render_template('index.html', blog_posts=response_json)


@app.route('/about.html')
def about_page():
    return render_template('about.html')


@app.route('/contact', methods=['POST', 'GET'])
def contact_page():
    if request.method == 'POST':
        message = 'Subject: A Contact Message was Sent\n\n'
        message += f"NAME: {request.form['username']}\nEMAIL: {request.form['email']}" \
                   f"\nPHONE: {request.form['phone']}\nMESSAGE: {request.form['message']}"

        try:
            with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as smtp_connection:
                smtp_connection.starttls()
                smtp_connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                smtp_connection.sendmail(from_addr=MY_EMAIL,
                                         to_addrs=MY_EMAIL,
                                         msg=message)
        except Exception as error_message:
            print(f'Something Went Wrong In Sending the Email:\n{error_message}')
        return render_template('contact.html', method=request.method)
    else:
        return render_template('contact.html', method=request.method)


@app.route('/post/<blog_id>')
def post_page(blog_id):
    page_post = {}
    for post in response_json:
        if post['id'] == int(blog_id):
            page_post = post
            break

    return render_template('post.html', page_post=page_post)


if __name__ == "__main__":
    app.run(debug=True)


