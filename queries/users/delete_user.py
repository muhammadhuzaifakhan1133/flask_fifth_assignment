def delete_customer_by_id(conn, user_id):
    query = f"DELETE FROM user WHERE id=%(user_id)s"
    cur = conn.cursor()
    isDeleted = cur.execute(query, {"user_id": user_id})
    conn.commit()
    return True if isDeleted == 1 else False