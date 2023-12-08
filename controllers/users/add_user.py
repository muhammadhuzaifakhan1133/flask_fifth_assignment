from queries.users import add_user as AddUser

def add_user_controller(db, email, phone, password, role_type):
    conn = db.connect()
    user_id = AddUser.add_user_query(conn, email, phone, password, role_type)
    db.disconnect(conn)
    return user_id