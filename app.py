from datetime import timedelta
from flask import Flask
from flask_jwt_extended import JWTManager
from routes.users import users_router_list
from routes.complaints import complaints_router_list
from routes.dashboards import dashboards_router_list
from services.file_services import UPLOAD_FOLDER
from services.response_services import display_response
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

app.secret_key = "o.=1A=e'$FH6S^EL;lQAQRa=5;w{{NlcuVOBpvkL^&2cQTYq)u"

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

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

@jwt.unauthorized_loader
def unauthorized_callback(jwt_payload):
    return display_response(status_code=400, errors=["Token is required"])


SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/swagger.json'  # Our API url (can of course be a local resource)

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    }
)

app.register_blueprint(swaggerui_blueprint)

for route in users_router_list:
    app.register_blueprint(route)

for route in complaints_router_list:
    app.register_blueprint(route)

for route in dashboards_router_list:
    app.register_blueprint(route)


if __name__  == "__main__":
    app.run(
        debug=True,
        port=3000
    )