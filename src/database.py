import sqlite3

DATABASE = "disaster.db"

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS districts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            province TEXT NOT NULL,
            latitude REAL NOT NULL,
            longitude REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_default_districts():
    districts = [
        ("Lahore", "Punjab", 31.5204, 74.3587),
        ("Karachi", "Sindh", 24.8607, 67.0011),
        ("Peshawar", "Khyber Pakhtunkhwa", 34.0151, 71.5249),
        ("Quetta", "Balochistan", 30.1798, 66.9750),
        ("Swat", "Khyber Pakhtunkhwa", 34.7717, 72.3600),
        ("Chitral", "Khyber Pakhtunkhwa", 35.8518, 71.7864),
    ]
    conn = get_connection()
    conn.executemany(
        "INSERT OR IGNORE INTO districts (name, province, latitude, longitude) "
        "VALUES (?, ?, ?, ?)",
        districts,
    )
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    add_default_districts()
    print("Database is ready.")
