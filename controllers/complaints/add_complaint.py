from queries.complaints import add_complaint as AddComplaint

def add_complaint_controller(db, title, description, complaint_type_id):
    conn = db.connect()
    complaint_id = AddComplaint.add_complaint_query(conn, title, description, complaint_type_id)
    db.disconnect(conn)
    return complaint_id