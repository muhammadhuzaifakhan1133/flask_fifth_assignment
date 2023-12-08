import pymysql


def connect():
    conn = pymysql.connect(
        host='huzaifakhan113.mysql.pythonanywhere-services.com',
        user='huzaifakhan113',
        password="cz5vYc2HQbmjfGT",
        db='complaint_management_system',
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn

def disconnect(conn):
    conn.close()
    