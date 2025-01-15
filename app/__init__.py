from flask import Flask, render_template, redirect
import random
from datetime import date

from .config import Configuration
from app.tweets import tweets
from form.form import TweetForm
from .models import db, Tweet
from flask_migrate import Migrate

app=Flask(__name__)
app.config.from_object(Configuration)
# sets up the connection
db.init_app(app)
Migrate(app, db)

@app.route('/')
def home():
    # this is where you owuld do DB stuff
    # tweet = random.choice(tweets)  # Randomly select a tweet
    # use below for dev.db
    tweets = Tweet.query.all()
    tweet = random.choice(tweets)
    return render_template("index.html", tweet=tweet)

@app.route('/feed')
def feed():
    tweets = Tweet.query.all()
    return render_template('feed.html', tweets=tweets)

@app.route("/new", methods=["GET", "POST"])
def new_tweet_form():
    form=TweetForm()

    if form.validate_on_submit():
        new_tweet={
           # "id": len(tweets)+1,
            "author": form.data["author"],
            "tweet": form.data["tweet"],
            "date": date.today(),
            "likes": 0
        }
        # tweets.append(new_tweet)

        # a new way of constructing the data
        new_tweet= Tweet(**new_tweet)
        db.session.add(new_tweet)
        db.session.commit()

        return redirect("/feed", 302)
    
    if form.errors:
        return form.errors

    return render_template("new_tweet.html", form=form)

