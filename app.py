from flask import Flask, request, render_template
import boto3

app = Flask(__name__)


comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')

@app.route("/", methods=["GET", "POST"])
def home():
    sentiment = None
    if request.method == "POST":
        text = request.form["text"]
        response = comprehend.detect_sentiment(Text=text, LanguageCode='en')
        sentiment = response['Sentiment']
    return render_template("index.html", sentiment=sentiment)

if __name__ == "__main__":
    app.run(debug=True)
