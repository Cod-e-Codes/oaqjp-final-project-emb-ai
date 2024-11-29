from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

# Create the Flask app
app = Flask(__name__)

@app.route('/')
def home():
    """
    Root route to confirm the app is running.
    Returns the index.html template with the form.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    try:
        # Get the text from the request JSON body
        data = request.get_json()

        if not data or 'text' not in data or not data['text'].strip():
            return jsonify({"error": "Invalid input! Please provide text to be analyzed."}), 400

        # Get the statement to analyze
        text_to_analyze = data['text']

        # Call the emotion detector function
        emotions = emotion_detector(text_to_analyze)

        if "error" in emotions:
            return jsonify({"error": f"Error in emotion detection: {emotions['error']}"}), 500

        if not any(emotions[key] is not None for key in emotions if key != 'dominant_emotion'):
            return jsonify({"error": "Unable to detect emotions. Please try with a different text."}), 400

        dominant_emotion = emotions['dominant_emotion']
        response_message = (
            f"For the given statement, the system response is 'anger': {emotions['anger']}, "
            f"'disgust': {emotions['disgust']}, 'fear': {emotions['fear']}, 'joy': {emotions['joy']}, "
            f"and 'sadness': {emotions['sadness']}. The dominant emotion is {dominant_emotion}."
        )

        return jsonify({"response": response_message})

    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}. Please try again later."}), 500



if __name__ == '__main__':
    # Start the Flask web server.
    app.run(debug=True, host='0.0.0.0', port=5000)
