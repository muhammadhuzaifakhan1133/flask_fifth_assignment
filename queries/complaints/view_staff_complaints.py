def view_staff_complaints_query(conn, status_id, user_id):
    query = "SELECT * FROM complaint WHERE complaint_status_id=%(status_id)s AND assignee_id=%(user_id)s"
    cur = conn.cursor()
    cur.execute(query, {
        "status_id":status_id,
        "user_id": user_id,
    })
    return cur.fetchall()