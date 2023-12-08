def assign_complaint_query(conn, complaint_id, user_id):
    cur = conn.cursor()
    query = f"SELECT id FROM user WHERE role_type='staff' AND id={user_id} AND is_available=1"
    cur.execute(query)
    user_data = cur.fetchone()
    if (user_data is None):
        return False
    query = "SELECT id FROM complaint_status WHERE name='ASSIGNED'"
    cur.execute(query)
    status_data = cur.fetchone()
    query = "UPDATE complaint SET assignee_id=%(user_id)s, complaint_status_id=%(complaint_status_id)s WHERE id=%(complaint_id)s"
    isUpdated = cur.execute(query, {
        "user_id": user_id,
        "complaint_id": complaint_id,
        "complaint_status_id": status_data.get("id"),
    })
    
    conn.commit()
    return True if isUpdated == 1 else False