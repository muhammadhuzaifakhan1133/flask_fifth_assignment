def login_user_query(conn, email, phone, password):
    query = "SELECT id, role_type FROM user"
    if (phone is not None):
        query += " WHERE phone_no=%(phone)s AND password=%(password)s"
    else:
        query += " WHERE email=%(email)s AND password=%(password)s"
    query += " AND role_type=1"
    print(query)
    cur = conn.cursor()
    cur.execute(query, {"email": email, "phone": phone, "password": password})
    return cur.fetchone()