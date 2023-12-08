def superadmin_dashboard_query(conn):
    cur = conn.cursor()
    query = "SELECT COUNT(*) AS staff_count FROM user WHERE role_type='staff'"
    cur.execute(query)
    data = cur.fetchone()
    staff_count = data.get('staff_count')
    query = "SELECT COUNT(*) AS admin_count FROM user WHERE role_type='admin'"
    cur.execute(query)
    data = cur.fetchone()
    admin_count = data.get('admin_count')
    query = "SELECT COUNT(*) AS total_seven_day_count FROM complaint WHERE created_at >=DATE(NOW() - INTERVAL 7 DAY)"
    cur.execute(query)
    data = cur.fetchone()
    total_seven_day_complaint_count = data.get('total_seven_day_count')
    query = "SELECT COUNT(*) AS resolved_seven_day_count FROM complaint WHERE created_at >=DATE(NOW() - INTERVAL 7 DAY) AND complaint_status_id=(SELECT id FROM complaint_status WHERE name='RESOLVED')"
    cur.execute(query)
    data = cur.fetchone()
    resolved_seven_day_complaint_count = data.get('resolved_seven_day_count')
    query = "SELECT COUNT(*) AS total_thirty_day_count FROM complaint WHERE created_at >=DATE(NOW() - INTERVAL 30 DAY)"
    cur.execute(query)
    data = cur.fetchone()
    total_thirty_day_complaint_count = data.get('total_thirty_day_count')
    query = "SELECT COUNT(*) AS resolved_thirty_day_count FROM complaint WHERE created_at >=DATE(NOW() - INTERVAL 30 DAY) AND complaint_status_id=(SELECT id FROM complaint_status WHERE name='RESOLVED')"
    cur.execute(query)
    data = cur.fetchone()
    resolved_thirty_day_complaint_count = data.get('resolved_thirty_day_count')
    query = "SELECT complaint_type_id, (SELECT name FROM complaint_type WHERE id=complaint_type_id LIMIT 1) as name, COUNT(*) AS count FROM complaint GROUP BY complaint_type_id ORDER BY count DESC LIMIT 5"
    cur.execute(query)
    top_five_complaint_statuses = cur.fetchall()
    return {
        "staff_count": staff_count,
        "admin_count": admin_count,
        "total_seven_day_complaint_count": total_seven_day_complaint_count,
        "resolved_seven_day_complaint_count": resolved_seven_day_complaint_count,
        "total_thirty_day_complaint_count": total_thirty_day_complaint_count,
        "resolved_thirty_day_complaint_count": resolved_thirty_day_complaint_count,
        "top_five_complaint_statuses": top_five_complaint_statuses
    }
