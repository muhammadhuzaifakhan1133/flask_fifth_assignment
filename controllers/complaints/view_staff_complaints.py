from queries.complaints import view_staff_complaints as ViewStaffComplaints

def view_staff_complaints_controller(db, status_id, user_id):
    conn = db.connect()
    complaints = ViewStaffComplaints.view_staff_complaints_query(conn, status_id, user_id)
    db.disconnect(conn)
    return complaints