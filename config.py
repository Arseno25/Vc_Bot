HEROKU = False  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku & Docker.
if HEROKU:
    from os import environ

    from dotenv import load_dotenv

    load_dotenv()  # take environment variables from .env.
    API_ID = int(environ["API_ID"])
    API_HASH = environ["API_HASH"]
    SESSION_STRING = environ["SESSION_STRING"]  # Check Readme for session
    ARQ_API_KEY = environ["ARQ_API_KEY"]
    DEFAULT_SERVICE = (
        environ["DEFAULT_SERVICE"]
        if "DEFAULT_SERVICE" in environ
        else "youtube"
    )

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID =6652699
    API_HASH = "9b91833676294630ece0f84fe45d4a34"
    ARQ_API_KEY = "XLAEYI-XHEJFW-UZSELN-CHGAVZ-ARQ"
    DEFAULT_SERVICE = "youtube"  # Must be one of "youtube"/"deezer"/"saavn"

# don't make changes below this line
ARQ_API = "https://thearq.tech"
