import requests
import json

def emotion_detector(text_to_analyze):
    if not text_to_analyze:
        # Return None for all keys when the input is empty
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Define the URL for the Watson Emotion API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Define the headers
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    # Define the input JSON
    data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Send the POST request to Watson NLP EmotionPredict endpoint
    response = requests.post(url, json=data, headers=headers)

    # Parse the response JSON
    response_json = response.json()

    # Initialize the emotions dictionary
    emotions = {
        'anger': 0.0,
        'disgust': 0.0,
        'fear': 0.0,
        'joy': 0.0,
        'sadness': 0.0
    }

    # Extract the emotion scores from the first prediction in the list
    try:
        emotion_data = response_json.get('emotionPredictions', [{}])[0].get('emotion', {})
        emotions['anger'] = emotion_data.get('anger', 0.0)
        emotions['disgust'] = emotion_data.get('disgust', 0.0)
        emotions['fear'] = emotion_data.get('fear', 0.0)
        emotions['joy'] = emotion_data.get('joy', 0.0)
        emotions['sadness'] = emotion_data.get('sadness', 0.0)
    except KeyError:
        return {"error": "Unable to parse emotion data"}

    # Determine the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Add dominant emotion to the dictionary
    emotions['dominant_emotion'] = dominant_emotion

    # Return the emotions with dominant emotion
    return emotions