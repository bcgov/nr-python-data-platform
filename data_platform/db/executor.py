import logging
from .db_connection import get_connection

def run_query(user, password, dsn, sql):
    connection = None
    try:
        connection = get_connection(user, password, dsn)
        cursor = connection.cursor()

        logging.info("Executing SQL query")
        cursor.execute(sql)

        rows = cursor.fetchall()

        cursor.close()
        return rows

    except Exception:
        logging.error("Query execution failed", exc_info=True)
        raise

    finally:
        if connection:
            connection.close()
            logging.info("Database connection closed")
