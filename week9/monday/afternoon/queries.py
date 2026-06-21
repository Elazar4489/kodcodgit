from db import get_connection

def get_by_rank(rank: str) -> dict | None:
    """
    SELECT * WHERE rank = %s
    :param rank:
    :return:
    """
    cnx = get_connection()
    my_cursor = cnx.cursor(dictionary=True)
    my_cursor.execute("SELECT DISTINCT `rank` FROM soldiers;")
    res = [obj["rank"] for obj in my_cursor.fetchall()]
    if rank in res:
        my_cursor.execute("SELECT * FROM soldiers WHERE `rank` = %s;", (rank,))
        by_rank = my_cursor.fetchall()
        cnx.close()
        my_cursor.close()
        return by_rank
    my_cursor.close()
    cnx.close()
    return None



def get_active_sorted(order: str) -> dict | None:
    """
    SELECT * WHERE active=TRUE ORDER BY name {order}
    :param order:
    :return:
    """
    order = order.upper()
    if order != "ASC" and order != "DESC":
        return None
    cnx = get_connection()
    my_cursor = cnx.cursor(dictionary=True)
    my_cursor.execute(f"SELECT * FROM soldiers WHERE active=TRUE ORDER BY name {order};")
    active_sorted = my_cursor.fetchall()
    cnx.close()
    my_cursor.close()
    return active_sorted


def get_distinct_units() -> dict:
    """
    SELECT DISTINCT unit
    :return:
    """
    cnx = get_connection()
    my_cursor = cnx.cursor(dictionary=True)
    my_cursor.execute(f"SELECT DISTINCT unit FROM soldiers;")
    distinct_units = my_cursor.fetchall()
    cnx.close()
    my_cursor.close()
    return distinct_units


def search_by_name(term: str) -> dict | None:
    """
    SELECT * WHERE name LIKE %s
    :return:
    """
    if "%" not in term:
        return None
    cnx = get_connection()
    my_cursor = cnx.cursor(dictionary=True)
    my_cursor.execute(f"SELECT *  FROM soldiers WHERE name LIKE %s;", (term,))
    by_name = my_cursor.fetchall()
    cnx.close()
    my_cursor.close()
    return by_name


def get_missing_rank() -> dict:
    """
    SELECT * WHERE rank IS NULL
    :return:
    """
    cnx = get_connection()
    my_cursor = cnx.cursor(dictionary=True)
    my_cursor.execute(f"SELECT *  FROM soldiers WHERE `rank` IS NULL;")
    missing_rank = my_cursor.fetchall()
    cnx.close()
    my_cursor.close()
    return missing_rank


def get_by_unit(unit: str) -> dict | None:
    """
    SELECT * WHERE unit = %s ORDER BY name ASC
    :return:
    """
    cnx = get_connection()
    my_cursor = cnx.cursor(dictionary=True)
    my_cursor.execute("SELECT DISTINCT `unit` FROM soldiers;")
    res = [obj["unit"] for obj in my_cursor.fetchall()]
    if unit in res:
        my_cursor.execute(f"SELECT *  FROM soldiers WHERE unit = %s ORDER BY name ASC;", (unit,))
        by_unit = my_cursor.fetchall()
        cnx.close()
        my_cursor.close()
        return by_unit
    cnx.close()
    my_cursor.close()
    return None

