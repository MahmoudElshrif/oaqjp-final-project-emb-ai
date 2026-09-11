"""Flask Server"""
from flask import Flask,request,render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def emotion_detection_route():
    """/emotionDetector api path"""
    text = request.args.get("textToAnalyze")

    detection = emotion_detector(text)
    anger = detection['anger']
    disgust = detection['disgust']
    fear = detection['fear']
    joy = detection['joy']
    sadness = detection['sadness']
    dominant_emotion = detection['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    formated_text = f"For the given statement, the system response is 'anger': {anger}"
    formated_text += f", 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
    formated_text += f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}."

    return formated_text


@app.route("/")
def home():
    """root page"""
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug = True,host="0.0.0.0",port=5000)
