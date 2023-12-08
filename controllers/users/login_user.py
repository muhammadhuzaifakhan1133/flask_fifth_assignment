from queries.users import login_user as LoginUser

def login_user_controller(db, email, phone, password):
    conn = db.connect()
    response = LoginUser.login_user_query(conn, email, phone, password)
    db.disconnect(conn)
    if (response is None): return None, None
    return response.get("id"), response.get("role_type")