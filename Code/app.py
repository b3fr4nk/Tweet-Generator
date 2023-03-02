"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template
from markov import Markov
from dictionary_words import *


app = Flask(__name__)

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.
corpus = "data/dickens.txt"
corpus = get_words_list(file=corpus)
chain = Markov(corpus)

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    text = chain.walk()

    return render_template("index.html", text=text)

if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
