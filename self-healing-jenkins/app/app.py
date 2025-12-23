from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Self-Healing CI/CD Pipeline Running"

app.run(host="0.0.0.0", port=5000)
