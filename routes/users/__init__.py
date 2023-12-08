from .login_user import login_user_bp
from .add_user import add_user_bp

users_router_list = []
users_router_list.append(login_user_bp)
users_router_list.append(add_user_bp)