import sqlite3

def createDB():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books_store (id INTEGER PRIMARY KEY, title TEXT, year INTEGER, author TEXT, isbn INTEGER)")
    conn.commit()
    conn.close()

def insertItem(title, year, author, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO books_store VALUES (NULL, ?, ?, ?, ?)", (title, year, author, isbn))
    conn.commit()
    conn.close()

def searchData(title="", year="", author="", isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books_store WHERE title=? OR year=? OR author=? OR isbn=?", (title, year, author, isbn))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def updateData(id, title, year, author, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE books_store SET title=?, year=?, author=?, isbn=? WHERE id=?", (title, year, author, isbn, id))
    conn.commit()
    conn.close()

def deleteData(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROm books_store WHERE id=?",(id,))
    conn.commit()
    conn.close()

def viewAll():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books_store")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows
