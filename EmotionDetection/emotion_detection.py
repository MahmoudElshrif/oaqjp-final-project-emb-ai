import requests
import json


def emotion_detector(text_to_analyze):
    
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyze } }
    
    
    response = requests.post(url,headers=headers,json=obj)
    
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }


    response_json = json.loads(response.text)

    emotions = ["anger","disgust","fear","joy","sadness"]


    emotions_score = {}

    dominant_emotion = ["",0]

    for i in emotions:
        score = response_json["emotionPredictions"][0]["emotion"][i]
        emotions_score[i] = score
        if(score > dominant_emotion[1]):
            dominant_emotion[0] = i
            dominant_emotion[1] = score
    
    emotions_score["dominant_emotion"] = dominant_emotion[0]

    return emotions_score

