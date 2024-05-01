"""A simple Flask service that returns a JSON response"""

from flask import Flask

app = Flask(__name__)

HELLO_MESSAGE = "Hello, world!"
GOODBYE_MESSAGE = "Goodbye, world!"
HELLO_NAME_MESSAGE = "Hello, {}!"
WEATHER_MESSAGE = "Nice weather, ain't it?"
DAY_MESSAGE = "Nice day, ain't it?"
CAT_MESSAGE = "Cats are pretty neat."


@app.route("/")
def hello_world():
    """
    Returns a dictionary with a message saying "Hello, world!".
    """
    return {"message": HELLO_MESSAGE}


@app.route("/goodbye")
def goodbye_world():
    """
    Returns a dictionary with a message saying "Goodbye, world!".
    """
    return {"message": GOODBYE_MESSAGE}


@app.route("/hello/<name>")
def hello_name(name):
    """
    Returns a dictionary with a message using the provided name.
    """
    return {"message": HELLO_NAME_MESSAGE.format(name)}


@app.route("/weather")
def weather():
    """
    Returns a dictionary with a message about the weather.
    """
    return {"message": WEATHER_MESSAGE}


@app.route("/nice-day")
def nice_day():
    """
    Returns a dictionary with a message saying "Nice day, ain't it?".
    """
    return {"message": DAY_MESSAGE}


@app.route("/cats")
def cats():
    """
    Returns a dictionary with a message saying "Cats are pretty neat.".
    """
    return {"message": CAT_MESSAGE}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
