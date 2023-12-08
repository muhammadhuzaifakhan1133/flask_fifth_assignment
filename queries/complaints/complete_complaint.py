def complete_complaint_query(conn, complaint_id):
    cur = conn.cursor()
    query = "SELECT id FROM complaint_status WHERE name='RESOLVED'"
    cur.execute(query)
    status_data = cur.fetchone()
    query = "UPDATE complaint SET complaint_status_id=%(complaint_status_id)s WHERE id=%(complaint_id)s"
    isUpdated = cur.execute(query, {
        "complaint_id": complaint_id,
        "complaint_status_id": status_data.get("id"),
    })
    conn.commit()
    return True if isUpdated == 1 else False