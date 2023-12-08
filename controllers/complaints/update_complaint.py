from queries.complaints import update_complaint as UpdateComplaint

def update_complaint_controller(db, id, title, description, complaint_type_id):
    conn = db.connect()
    isUpdated = UpdateComplaint.update_complaint_query(conn, id, title, description, complaint_type_id)
    db.disconnect(conn)
    return isUpdated