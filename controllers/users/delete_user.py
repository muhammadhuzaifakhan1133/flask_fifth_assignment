from queries.users import delete_user as DeleteUser

def delete_user_controller(db, id):
    conn = db.connect()
    isDeleted = DeleteUser.delete_customer_by_id(conn, id)
    db.disconnect(conn)
    return isDeleted