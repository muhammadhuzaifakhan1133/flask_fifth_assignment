from queries.complaints import add_complaint_type as AddComplaintType

def add_complaint_type_controller(db, name):
    conn = db.connect()
    type_id = AddComplaintType.add_complaint_type_query(conn, name)
    db.disconnect(conn)
    return type_id