def update_user_query(conn, id, email, phone, password, role_type):
    query = "UPDATE user SET "
    if email is not None:
        query += "email=%(email)s,"
    if phone is not None:
        query += "phone_no=%(phone)s,"
    if password is not None:
        query += "password=%(password)s,"
    if role_type is not None:
        query += "role_type=%(role_type)s,"
    query = query[:-1]
    query += " WHERE id=%(id)s"
    cur = conn.cursor()
    isUpdated = cur.execute(query, {
        "id": id,
        "email": email,
        "phone": phone,
        "password": password,
        "role_type": role_type,
    })
    conn.commit()
    return True if isUpdated == 1 else False