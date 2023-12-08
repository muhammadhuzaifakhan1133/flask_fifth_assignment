from queries.complaints import done_complaint as DoneComplaint

def done_complaint_controller(db, complaint_id, filename):
    conn = db.connect()
    isUpdated = DoneComplaint.done_complaint_query(conn, complaint_id, filename)
    db.disconnect(conn)
    return isUpdated
