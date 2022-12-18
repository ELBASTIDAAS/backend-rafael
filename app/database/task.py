from app.database import get_db


def output_formater(results):
    out = []
    for result in results:
        formatted_result = {
            'id': result[0],
            'summary': result[1],
            'description': result[2],
            'is_active': result[3],
        }
        out.append(formatted_result)
    return out


def scan():
    conn = get_db()
    cursor = conn.execute(
        "SELECT * FROM task WHERE is_active = 1", ()
    )
    results = cursor.fetchall()
    cursor.close()
    return output_formater(results)


def select_by_id(pk):
    conn = get_db()
    cursor = conn.execute(
        "SELECT * FROM task WHERE id = ?", (pk,)
    )
    results = cursor.fetchall()
    cursor.close()
    return output_formater(results)


def insert(raw_data):
    task_data = (
        raw_data('summary'),
        raw_data('description'),
    )
    statement = """
    INSERT INTO task (
        summary, 
        description
        ) VALUES (
            ?, ?
        )
    """
    conn = get_db()
    conn.execute(statement, task_data)
    conn.commit()
    conn.close()


def update(raw_data, pk):
    task_data = (
        raw_data('summary'),
        raw_data('description'),
        raw_data('is_active'),
        pk,
    )
    statement = """
    UPDATE task SET 
        summary = ?, 
        description = ?
        is_active = ?
    WHERE id = ?
    """
    conn = get_db()
    conn.execute(statement, task_data)
    conn.commit()
    conn.close()


def delete(pk):
    conn = get_db()
    conn.execute(
        "DELETE FROM task WHERE id = ?", (pk,)
    )
    conn.commit()
    conn.close()
