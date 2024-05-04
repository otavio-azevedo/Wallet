import psycopg2
import constants


def get_db_connection():
    return psycopg2.connect(database=constants.DATABASE_NAME,
                            host=constants.DATABASE_HOST,
                            user=constants.DATABASE_USER,
                            password=constants.DATABASE_PASSWORD,
                            port=constants.DATABASE_PORT)
