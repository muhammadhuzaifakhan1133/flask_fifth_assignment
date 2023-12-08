from queries.complaints import complete_complaint as CompleteComplaint

def complete_complaint_controller(db, complaint_id):
    conn = db.connect()
    isUpdated = CompleteComplaint.complete_complaint_query(conn, complaint_id)
    db.disconnect(conn)
    return isUpdated