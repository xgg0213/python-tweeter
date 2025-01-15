import os

class Configuration:
    SECRET_KEY=os.environ.get("SECRET_KEY")
    #define any other secret environment variables here
    SQLALCHEMY_DATABASE_URI= os.environ.get("DATABASE_URL")
    #turn it off to save stoarge and avoid using unnecessary resources
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    