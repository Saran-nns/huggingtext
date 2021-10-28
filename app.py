
from flask import Flask, request, render_template
from sentimentmodel import SentimentModel

app = Flask(__name__)
model = SentimentModel()


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def index_post():

    # Read the values from the form
    original_text = request.form["text"]

    # Retrieve the sentiment
    sentiment = model.predict_sentiment([original_text])


    # Call render template, passing the sentiment text and original text
    return render_template(
        "results.html",
        sentiment=sentiment,
        original_text=original_text,
    )

if __name__ == "__main__":

    app.run(host="0.0.0.0", port="5000", debug=True)
