import sqlite3

__connection = None

def get_connection():
    global __connection
    if __connection is None:
        __connection = sqlite3.connect('anketa.db')
    return __connection

def init_db(force: bool = False):
    conn = get_connection()

    c = conn.cursor()

    # удалить таблицу user_message, если она существует
    if force:
        c.execute('DROP TABLE IF EXISTS user_message')

    c.execute('''
        CREATE TABLE IF NOT EXISTS user_message (
            id          INTEGER PRIMARY KEY,
            user_id     INTEGER NOT NULL,
            text        TEXT NOT NULL
        )
    ''')
    conn.commit()

def add_message(user_id: int, text: str):
    conn = get_connection()
    c = conn.cursor()
    c.execute('INSERT INTO user_message (user_id, text) VALUES (?, ?)', (user_id, text))
    conn.commit()

def count_messages(user_id: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM user_message WHERE user_id = ?', (user_id, ))
    (res, ) = c.fetchall()
    conn.commit()
    return res

def list_messages(user_id: int, limit: int = 10):
    conn = get_connection()
    c = conn.cursor()

    c.execute('SELECT id, text FROM user_message WHERE user_id = ? ORDER BY id DESC LIMIT ?', (user_id, limit))
    return c.fetchall()

if __name__ == '__main__':
    init_db(force=False)
    r = count_messages(user_id=12344)
    print(r)
    r = list_messages(user_id=12344, limit=2)
    [print(item) for item in r]