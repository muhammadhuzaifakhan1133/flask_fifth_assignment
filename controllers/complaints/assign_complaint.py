from queries.complaints import assign_complaint as AssignComplaint

def assign_complaint_controller(db, complaint_id, user_id):
    conn = db.connect()
    isUpdated = AssignComplaint.assign_complaint_query(conn, complaint_id, user_id)
    db.disconnect(conn)
    return isUpdated