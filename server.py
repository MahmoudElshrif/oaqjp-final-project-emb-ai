from flask import Flask,request,render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def emotionDetector():
    text = request.args.get("textToAnalyze")

    detection = emotion_detector(text)
    anger = detection['anger']
    disgust = detection['disgust']
    fear = detection['fear']
    joy = detection['joy']
    sadness = detection['sadness']
    dominant_emotion = detection['dominant_emotion']

    formated_text = f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."

    return formated_text


@app.route("/")
def home():
    return render_template("index.html")


if(__name__ == '__main__'):
    app.run(debug = True,host="0.0.0.0",port=5000)