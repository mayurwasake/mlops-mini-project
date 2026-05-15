from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World! This is the home page of the Flask app."

app.run(debug=True)