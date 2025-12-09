import requests
import json

def emotion_detector(text_to_analyze:str):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    result = json.loads(response.text)

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

    return emotions