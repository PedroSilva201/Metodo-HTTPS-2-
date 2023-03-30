from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Bom dia Vale!"
if __name__ == "__main__":
    app.run(ssl_context='adhoc')