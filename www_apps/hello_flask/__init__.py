from flask import Flask
app = Flask(__name__)


@app.route("/")
@app.route("/hello", strict_slashes=False, methods=["GET"])
@app.route("/flask", strict_slashes=False, methods=["GET"])
@app.route("/hello_flask", strict_slashes=False, methods=["GET"])
def hello():
    return "Hello from Flask!"


if __name__ == "__main__":
    app.run()
