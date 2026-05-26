from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return {
        "status": "success",
        "message": "API Running"
    }