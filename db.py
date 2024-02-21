import sqlite3


class DBShop:
    def __init__(self, db_name):
        self.connect = sqlite3.connect(f"{db_name}.db")
        self.cursor = self.connect.cursor()

    def create(self):
        sql = """
        CREATE TABLE IF NOT EXISTS USER(
            id INTEGER PRIMARY KEY,
            username VARCHAR(20),
            password VARCHAR(256),
            balance INTEGER DEFAULT 0)"""
        self.cursor.execute(sql)
        sql = """
        CREATE TABLE IF NOT EXISTS PRODUCT(
            id INTEGER PRIMARY KEY,
            name VARCHAR(30),
            count INTEGER DEFAULT 0,
            price INTEGER NOT NULL)"""
        self.cursor.execute(sql)
        self.connect.commit()

    def add_user(self, username: str, password: str):
        sql = """SELECT id FROM USER WHERE username = (?)"""
        user = self.cursor.execute(sql, (username,)).fetchone()
        if user is not None:
            raise Exception("не возможно добавить пользователь уже есть")
        else:
            sql = """INSERT INTO USER (username, password) VALUES (?, ?)"""
            self.cursor.execute(sql, (username, password))
            self.connect.commit()

    def add_product(self, name, count, price):
        sql = """SELECT id FROM PRODUCT WHERE name = (?)"""
        user = self.cursor.execute(sql, (name,)).fetchone()
        if user is not None:
            raise Exception("не возможно добавить товар уже есть")
        else:
            sql = """INSERT INTO PRODUCT (name, count, price) VALUES (?, ?, ?)"""
            self.cursor.execute(sql, (name, count, price))
            self.connect.commit()

    def close(self):
        self.connect.close()
