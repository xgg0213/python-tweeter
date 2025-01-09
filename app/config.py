import os

class Configuration:
    SECRET_KEY=os.environ.get("SECRET_KEY")
    #define any other secret environment variables here
    