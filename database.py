import sqlite3

def get_db():
    conn = sqlite3.connect('inventory.db')
    return conn

def init_db():
    conn = get_db()
    c = conn.cursor()
    # প্রোডাক্ট টেবিল
    c.execute('''CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    buy_price REAL NOT NULL,
                    sell_price REAL NOT NULL,
                    stock INTEGER DEFAULT 0
                )''')
    # লেনদেন টেবিল (কেনা/বিক্রি)
    c.execute('''CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_id INTEGER,
                    type TEXT, -- 'BUY' or 'SELL'
                    quantity INTEGER,
                    total_price REAL,
                    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY(product_id) REFERENCES products(id)
                )''')
    conn.commit()
    conn.close()
