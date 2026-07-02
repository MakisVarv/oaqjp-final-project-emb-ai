import json
import requests
def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    response = requests.post(url, json=input_json, headers=headers, timeout=10)
    response_data = json.loads(response.text)
    emotion_scores = response_data["emotionPredictions"][0]["emotion"]
    dominant_emotion = None
    highest_score = 0

    for emotion, score in emotion_scores.items():
        if score > highest_score:
            highest_score = score
            dominant_emotion = emotion
    return {
    "anger": emotion_scores["anger"],
    "disgust": emotion_scores["disgust"],
    "fear": emotion_scores["fear"],
    "joy": emotion_scores["joy"],
    "sadness": emotion_scores["sadness"],
    "dominant_emotion": dominant_emotion,
}