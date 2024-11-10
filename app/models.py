import sqlite3

def get_db_connection():
    conn = sqlite3.connect("urls.db")
    conn.row_factory = sqlite3.Row  
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            long_url TEXT NOT NULL,
            short_code TEXT NOT NULL UNIQUE
        )
    ''')
    
    conn.commit()
    conn.close()

def insert_url(long_url, short_code):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO urls (long_url, short_code)
        VALUES (?, ?)
    ''', (long_url, short_code))


    conn.commit()
    conn.close()

def get_url_by_code(short_code):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT long_url FROM urls WHERE short_code = ?
    ''', (short_code,))
    result = cursor.fetchone()
    
    conn.close()

    if result:
        return result['long_url']
    return None