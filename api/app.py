from flask import Flask, render_template, request, jsonify
from recommendation_engine.rules import analyze_soil

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")



    data = request.json

    result = analyze_soil(data)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)


@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.json

    result = analyze_soil(data)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)

app = app