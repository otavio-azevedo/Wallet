from psycopg2.extras import execute_batch
from ..connection import get_db_connection
from . import mappers


def bulk_insert(data):
    sql = "INSERT INTO statement_history (transaction_date, origin, operation, amount, balance) VALUES (%s, %s, %s, %s, %s)"

    statements = data.apply(mappers.map_statements, axis=1)

    with get_db_connection() as conn:
        with conn.cursor() as cur:
            execute_batch(cur, sql, statements)
