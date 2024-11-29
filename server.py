"""
This module defines a Flask web server that serves an emotion detection API.
It processes text input and returns emotion analysis using the Watson Emotion API.
"""

from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

# Create the Flask app
app = Flask(__name__)

@app.route('/')
def home():
    """
    Root route to confirm the app is running.
    Returns a simple message indicating the API is working.
    """
    return "Emotion Detection API is running. Send a POST request to /emotionDetector."

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    """
    Handles POST requests to the /emotionDetector endpoint.
    This function processes the input text, analyzes emotions using the emotion_detector function,
    and returns the emotion analysis result as a formatted response.

    Returns:
        Response: A JSON response containing the emotion analysis.
    """
    # Get the text from the request JSON body
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({"error": "No text provided"}), 400

    # Get the statement to analyze
    text_to_analyze = data['text']

    # Call the emotion detector function
    emotions = emotion_detector(text_to_analyze)

    # Create the output response message in the required format
    dominant_emotion = emotions['dominant_emotion']
    response_message = (
        f"For the given statement, the system response is 'anger': {emotions['anger']}, "
        f"'disgust': {emotions['disgust']}, 'fear': {emotions['fear']}, 'joy': {emotions['joy']}, "
        f"and 'sadness': {emotions['sadness']}. The dominant emotion is {dominant_emotion}."
    )

    # Return the response
    return jsonify({"response": response_message})

if __name__ == '__main__':
    # Start the Flask web server.
    # Runs the application on localhost:5000.
    app.run(debug=True, host='0.0.0.0', port=5000)
