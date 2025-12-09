"""
Server script for AI Emotion Detection
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask ("Emotion Detection")

@app.route("/emotionDetector")
def sent_detector():
    """
    Entrypoint for emotion Detector
    """
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again"
    return f"For the given statement, the system response is {response}"

@app.route("/")
def render_indexpage():
    """
    Main entrypoint
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
