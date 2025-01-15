from dotenv import load_dotenv
from datetime import date

from app import app
from app.models import db, Tweet

with app.app_context():
    db.create_all()

    seed_tweet=Tweet(
        tweet="test tweet",
        author="test author",
        date=date.today(),
        likes=0
    )

    # 
    db.session.add(seed_tweet)
    db.session.commit()