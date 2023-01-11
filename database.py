import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None 
    try: 
        conn = sqlite3.connect(db_file)
        return conn

    except Error as e: 
        print(e)

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
    
def main():
    database = r"C:\Users\svenh\OneDrive - Bildungszentrum Zürichsee\BZZ\Maurizi\Modul242\WebScrap\database_webscrape.db"

    sql_create_main_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        store text,
                                        datetime text,
                                        price text
                                    ); """
                                    
    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_main_table)
    else:
        print("Error! can not creat the database connection")


if __name__ == '__main__':
    main()