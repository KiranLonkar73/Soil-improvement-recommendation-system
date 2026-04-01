import os
from flask import Flask, render_template, request, jsonify
from recommendation_engine.rules import analyze_soil


# Correct Flask initialization for Render deployment
app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), "../templates"),
    static_folder=os.path.join(os.path.dirname(__file__), "../static")
)


# Homepage route (ONLY ONE allowed)
@app.route("/")
def home():
    return render_template("index.html")


# Prediction route
@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    result = analyze_soil(data)
    return jsonify(result)


# Required for gunicorn
app = app