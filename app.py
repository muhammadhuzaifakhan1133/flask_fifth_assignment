from datetime import timedelta
from flask import Flask
from flask_jwt_extended import JWTManager
from routes.users import users_router_list
from services.response_services import display_response

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "o.=1A=e'$FH6S^EL;lQAQRa=5;w{{NlcuVOBpvkL^&2cQTYq)u"  # Change this!
app.config["JWT_TOKEN_LOCATION"] = ["headers"] # specifying the location of JWT 
app.config["JWT_ALGORITHM"] = "HS256" # symmetric keyed hashing algorithm
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)

jwt = JWTManager(app)

@jwt.invalid_token_loader
def invalid_token_callback(jwt_payload):
    return display_response(status_code=400, errors=["Invalid Token"])

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return display_response(status_code=400, errors=["Expired Token"])


for route in users_router_list:
    app.register_blueprint(route)



if __name__  == "__main__":
    app.run(
        debug=True,
        port=3000
    )