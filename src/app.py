from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Pakistan Disaster Management System: test page is working!"

if __name__ == "__main__":
    app.run(debug=True)
