import psycopg2 as psql
from typing import List, Tuple, Any

import config

conn = psql.connect(config.DATABASE_URI)


def get_orders() -> List[Tuple[Any]]:
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM orders;"
    )
    data = cur.fetchall()
    return data
