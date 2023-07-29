import sqlite3 as sql



async def create_tables():
    con = sql.connect("register.db")
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS students(
                fio TEXT,
                age INTEGER,
                phone_number TEXT
    )""")

