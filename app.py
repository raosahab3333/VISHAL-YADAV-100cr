from flask import Flask, render_template
from strategy import scan_stocks

app = Flask(__name__)

@app.route("/")
def home():
    results = scan_stocks()
    return render_template("index.html", stocks=results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)