# Emotion Detection API

This is a Flask-based API that analyzes emotions in a given text using the Watson Emotion API. It accepts POST requests containing text and returns a detailed analysis of emotions like anger, disgust, fear, joy, and sadness, along with the dominant emotion.

## Features
- Detects multiple emotions from text input: anger, disgust, fear, joy, and sadness.
- Returns a response with the emotion scores and dominant emotion.
- Handles blank or missing text input gracefully with appropriate error handling.

## Installation and Setup

### Prerequisites
- Python 3.7+ installed on your machine.
- A virtual environment (recommended).

### Steps to Set Up

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/emotion-detection-api.git
    cd emotion-detection-api
    ```

2. **Set up a virtual environment**:
    - If you're using `venv`:
        ```bash
        python -m venv venv
        source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
        ```

3. **Install dependencies**:
    - Install the necessary Python libraries using `pip`:
        ```bash
        pip install -r requirements.txt
        ```

4. **Run the application**:
    - After installing the dependencies, run the Flask app:
        ```bash
        python server.py
        ```

    - The application will be available at `http://127.0.0.1:5000/`.

### Usage

- Send a `POST` request to `/emotionDetector` with a JSON body containing the text to be analyzed.

#### Example request:
```bash
curl -X POST http://127.0.0.1:5000/emotionDetector \
-H "Content-Type: application/json" \
-d '{"text": "I am so happy today!"}'
```

#### Example response:
```json
{
  "response": "For the given statement, the system response is 'anger': 0.0, 'disgust': 0.0, 'fear': 0.0, 'joy': 0.95, and 'sadness': 0.0. The dominant emotion is joy."
}
```

### Error Handling

If no text is provided, the API will return a 400 Bad Request status with an appropriate error message.

#### Example:
```json
{
  "error": "No text provided"
}
```

### Static Code Analysis

The project has been statically analyzed using PyLint with a high compliance score of 9.41/10.

### Deployment

You can deploy the app to a cloud provider like Heroku or AWS using the Flask deployment guides for each respective platform.

### Contributing

If you want to contribute to this project, feel free to fork the repository, make changes, and submit a pull request.

### License

This project is licensed under the Apache 2.0 License - see the LICENSE file for details.
