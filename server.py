"""
This module sets up a Flask web application for emotion detection.
It provides an endpoint to analyze text and return emotion scores 
along with the dominant emotion detected.
"""
from flask import Flask, render_template, request  # Removed jsonify as it's not used
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Retrieve the text to analyze from the request arguments and apply emotion analysis.
    Returns a formatted string with the emotion scores and dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    # Check for invalid text
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    # Format the response string
    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )
@app.route("/")
def render_index_page():
    """
    Render the index.html page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)