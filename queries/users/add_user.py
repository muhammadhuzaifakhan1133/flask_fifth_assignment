def add_user_query(conn, email, phone, password, role_type):
    query = """
            INSERT INTO user (email, phone_no, password, role_type)
            VALUES (%(email)s, %(phone)s, %(password)s, %(role_type)s)
        """
    cur = conn.cursor()
    cur.execute(query, {
        "email": email,
        "phone": phone,
        "password": password,
        "role_type": role_type,
    })
    conn.commit()
    return cur.lastrowid