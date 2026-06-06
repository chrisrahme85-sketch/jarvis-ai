from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>JARVIS ONLINE</h1>
    <p>Hello Sir.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
