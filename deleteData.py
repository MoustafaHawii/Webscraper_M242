import sqlite3




def delete_all_tasks(conn):
    """
    Delete all rows in the projects table
    :param conn: Connection to the SQLite database
    :return:
    """
    sql = 'DELETE FROM projects'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def main():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    database = r"database.db"

    # create a database connection
    conn = delete_all_tasks(conn)
    with conn:
        delete_all_tasks(conn)
        # delete_all_tasks(conn);


if __name__ == '__main__':
    main()
