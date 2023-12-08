import pymysql


def connect():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="root",
        db='complaint_management_system',
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn

def disconnect(conn):
    conn.close()
    