def add_complaint_query(conn, title, description, complaint_type_id):
    query = "SELECT id FROM complaint_status WHERE name='PENDING'"
    cur = conn.cursor()
    cur.execute(query)
    data = cur.fetchone()
    pending_id = data.get("id")
    query = """
            INSERT INTO complaint (title, description, complaint_type_id, complaint_status_id)
            VALUES (%(title)s, %(description)s, %(complaint_type_id)s, %(complaint_status_id)s)
            """
    cur = conn.cursor()
    cur.execute(query, {
        "title": title,
        "description": description,
        "complaint_type_id": complaint_type_id,
        "complaint_status_id": pending_id,
    })
    conn.commit()
    return cur.lastrowid