def update_complaint_query(conn, id, title, description, complaint_type_id):
    query = "UPDATE complaint SET "
    if title is not None:
        query += "title=%(title)s,"
    if description is not None:
        query += "description_no=%(description)s,"
    if complaint_type_id is not None:
        query += "complaint_type_id=%(complaint_type_id)s,"
    query = query[:-1]
    query += " WHERE id=%(id)s"
    cur = conn.cursor()
    isUpdated = cur.execute(query, {
        "id": id,
        "title": title,
        "description": description,
        "complaint_type_id": complaint_type_id,
    })
    conn.commit()
    return True if isUpdated == 1 else False