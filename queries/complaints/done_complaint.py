def done_complaint_query(conn, complaint_id, filename):
    cur = conn.cursor()
    query = "SELECT id FROM complaint_status WHERE name='DONE'"
    cur.execute(query)
    status_data = cur.fetchone()
    query = "UPDATE complaint SET complaint_status_id=%(complaint_status_id)s, file_url=%(filename)s WHERE id=%(complaint_id)s"
    isUpdated = cur.execute(query, {
        "complaint_id": complaint_id,
        "complaint_status_id": status_data.get("id"),
        "filename": filename,
    })
    conn.commit()
    return True if isUpdated == 1 else False