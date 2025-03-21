''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
from flask import Flask, render_template, request
# Import the emotion_detector function from the package created: TODO
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This function analice the emotions
    '''
    text_to_analyze = request.args.get("textToAnalyze")

    if text_to_analyze == '':
        return "Invalid text! Please try again!"

    response = emotion_detector(text_to_analyze)

    # Verifica si el label es None, lo que indica un error o entrada no válida
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Devolver una cadena formateada con la etiqueta de sentimiento y la puntuación
    return f"For the given statement, the system response is \
            'anger': {response['anger']}, \
            'disgust': {response['disgust']}, \
            'fear': {response['fear']}, \
            'joy': {response['joy']} and 'sadness': {response['sadness']}. \
            The dominant emotion is {response['dominant_emotion']}."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    # This funtions executes the flask app and deploys it on localhost:5000
    app.run(debug=True)
