from queries.dashboards import superadmin_dashboards as SuperAdminDashboard

def superadmin_dashboard_controller(db):
    conn = db.connect()
    counts = SuperAdminDashboard.superadmin_dashboard_query(conn)
    db.disconnect(conn)
    return counts