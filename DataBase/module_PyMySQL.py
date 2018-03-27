import pymysql


def sql_connection():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        passwd='root',
        db='mysql',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)

    return conn


def sql_insert(conn):
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO users (email, password) VALUES(%s, %s)"
            cursor.execute(sql, ('sigld1004@naver.com', 'secret'))

        conn.commit()

    finally:
        conn.close()


def sql_select(conn):
    try:
        with conn.cursor() as cursor:
            sql = "SELECT id, password FROM users WHERE email=%s"
            cursor.execute(sql, ('sigld1004@naver.com',))
            result = cursor.fetchone()
            print(result)

    finally:
        conn.close()


def sql_delete(conn):
    try:
        with conn.cursor() as cursor:
            sql = "DELETE FROM users WHERE email=%s"
            cursor.execute(sql, ('sigld1004@naver.com',))

        conn.commit()

    finally:
        conn.close()


if __name__ == '__main__':
    # sql_insert(sql_connection())
    # sql_delete(sql_connection())
    sql_select(sql_connection())
