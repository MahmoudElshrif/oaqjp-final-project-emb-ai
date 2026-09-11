from flask import Flask,request,render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def emotionDetector():
    text = request.args.get("textToAnalyze")

    detection = emotion_detector(text)
    formated_text = f"For the given statement, the system response is 'anger': {detection["anger"]}, 'disgust': {detection["disgust"]}, 'fear': {detection["fear"]}, 'joy': {detection["joy"]} and 'sadness': {detection["sadness"]}. The dominant emotion is {detection["dominant_emotion"]}. "
    return formated_text


@app.route("/")
def home():
    return render_template("index.html")


if(__name__ == '__main__'):
    app.run(debug = True)