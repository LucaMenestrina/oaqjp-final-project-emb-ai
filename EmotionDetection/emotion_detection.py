import requests
import json

def emotion_detector(text_to_analyze:str):
    """
    Emotion detector based on IBM AI
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    result = json.loads(response.text)

    if response.status_code == 200:
        scores = result["emotionPredictions"][0]["emotion"]

        anger_score = scores["anger"]
        disgust_score = scores["disgust"]
        fear_score = scores["fear"]
        joy_score = scores["joy"]
        sadness_score = scores["sadness"]
        dominant_emotion = max(scores, key=lambda k: scores[k])

        emotions = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
    elif response.status_code == 400:
        emotions = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    return emotions