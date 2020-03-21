import sqlite3

def drop_table():
  with sqlite3.connect('coffee.db') as connection:
    c = connection.cursor()
    c.execute("""DROP TABLE IF EXISTS coffee;""")
  return True

def create_db():
  with sqlite3.connect('coffee.db') as connection:
    c = connection.cursor()
    table = """CREATE TABLE coffee(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      roast INTEGER NOT NULL,
      coffeename TEXT NOT NULL,
      waterweight INTEGER NOT NULL,
      coffeeweight INTEGER NOT NULL,
      watertemp INTEGER NOT NULL,
      grind INTEGER NOT NULL,
      brewtime INTEGER NOT NULL
    );
    """
    c.execute(table)
  return True

if __name__ == '__main__':
  drop_table()
  create_db()