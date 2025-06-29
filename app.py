from flask import Flask, render_template
from strategy import scan_stocks

app = Flask(__name__)

@app.route("/")
def home():
    results = scan_stocks()
    return render_template("index.html", stocks=results)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
