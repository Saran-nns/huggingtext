
from flask import Flask, request, render_template
from sentimentmodel import SentimentModel

app = Flask(__name__)
model = SentimentModel()


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


# code
@app.route("/", methods=["POST"])
def index_post():

    # Read the values from the form
    original_text = request.form["text"]

    # Retrieve the translation

    if type(original_text)==str:

        translated_text = model.predict_sentiment(tuple(original_text))


    # Call render template, passing the translated text,
    # original text, and target language to the template
    return render_template(
        "results.html",
        translated_text=translated_text,
        original_text=original_text,
    )

if __name__ == "__main__":

    app.run(host="127.0.0.1", port="5000", debug=True)
