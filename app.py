from datetime import timedelta
from flask import Flask
from flask_jwt_extended import JWTManager


app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "o.=1A=e'$FH6S^EL;lQAQRa=5;w{{NlcuVOBpvkL^&2cQTYq)u"  # Change this!
app.config["JWT_TOKEN_LOCATION"] = ["headers"] # specifying the location of JWT 
app.config["JWT_ALGORITHM"] = "HS256" # symmetric keyed hashing algorithm
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)

jwt = JWTManager(app)


if __name__  == "__main__":
    app.run(
        debug=True,
        port=3000
    )