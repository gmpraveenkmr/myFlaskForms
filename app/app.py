from flask import Flask, render_template, request

subscribers = []
app1 = Flask(__name__)


@app1.route('/')
def index():
    title = "Welcome to my Home!"
    return render_template('index.html', title=title)


@app1.route('/subscribe')
def subscribe():
    title = "Subscribe to my Channel"
    return render_template('subscribe.html', title=title)


@app1.route('/form', methods=["POST"])
def form():
    title = "Thanks for subscribing!"
    first_name = request.form.get('fname')
    last_name = request.form.get('lname')
    email = request.form.get('email')
    subscribers.append(f"{first_name} {last_name} {email}")
    return render_template('form.html', title=title, subscribers=subscribers)
