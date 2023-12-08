def add_complaint_type_query(conn, name):
    query = "INSERT INTO complaint_type (name) VALUE (%(name)s)"
    cur = conn.cursor()
    cur.execute(query, {
        "name": name,
    })
    conn.commit()
    return cur.lastrowid