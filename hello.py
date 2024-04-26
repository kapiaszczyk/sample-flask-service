"""A simple Flask service that returns a JSON response"""

from flask import Flask

app = Flask(__name__)

HELLO_MESSAGE = "Hello, world!"


@app.route("/")
def hello_world():
    """
    Returns a dictionary with a message saying "Hello, world!".
    """
    return {"message": HELLO_MESSAGE}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
