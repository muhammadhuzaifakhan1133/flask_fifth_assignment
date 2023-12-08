from queries.users import update_user as UpdateUser

def update_user_controller(db, id, email, phone, password, role_type):
    conn = db.connect()
    isUpdated = UpdateUser.update_user_query(conn,id, email, phone, password, role_type)
    db.disconnect(conn)
    return isUpdated