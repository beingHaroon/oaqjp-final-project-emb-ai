import requests
import json

def emotion_detector(text_to_analyze):
    if not text_to_analyze:
        # Return None for all emotions if the input is empty
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    payload = {
        "rawDocument": {
            "text": text_to_analyze
        }
    }
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    # Handle the 400 error by returning None for all emotions
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    if response.status_code != 200:
        return f"Error: Received status code {response.status_code}"

    formatted_response = response.json()
    if 'emotionPredictions' in formatted_response:
        emotion_data = formatted_response['emotionPredictions'][0]['emotion']
        anger_score = emotion_data.get('anger', 0)
        disgust_score = emotion_data.get('disgust', 0)
        fear_score = emotion_data.get('fear', 0)
        joy_score = emotion_data.get('joy', 0)
        sadness_score = emotion_data.get('sadness', 0)

        emotion_scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }

        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
    else:
        return "Error: 'emotionPredictions' not found in the response."
