from flask import Flask, render_template
import random
from .config import Configuration
from app.tweets import tweets

app=Flask(__name__)
app.config.from_object(Configuration)

@app.route('/')
def home():
    # this is where you owuld do DB stuff
    tweet = random.choice(tweets)  # Randomly select a tweet
    return render_template("index.html", tweet=tweet)

@app.route('/feed')
def feed():
    return render_template('feed.html', tweets=tweets)

