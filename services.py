from database import get_db

def add_product(name, buy_price, sell_price):
    conn = get_db()
    c = conn.cursor()
    c.execute("INSERT INTO products (name, buy_price, sell_price) VALUES (?, ?, ?)", (name, buy_price, sell_price))
    conn.commit()
    conn.close()
    print("✅ প্রোডাক্ট যোগ করা হয়েছে!")

def purchase_stock(product_id, quantity, buy_price):
    conn = get_db()
    c = conn.cursor()
    total = quantity * buy_price
    c.execute("UPDATE products SET stock = stock + ? WHERE id = ?", (quantity, product_id))
    c.execute("INSERT INTO transactions (product_id, type, quantity, total_price) VALUES (?, 'BUY', ?, ?)", (product_id, quantity, total))
    conn.commit()
    conn.close()
    print(f"✅ {quantity} পিস মাল কেনা হয়েছে। মোট খরচ: {total} টাকা")

def sell_product(product_id, quantity):
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT stock, sell_price FROM products WHERE id = ?", (product_id,))
    result = c.fetchone()
    if result and result[0] >= quantity:
        total = quantity * result[1]
        c.execute("UPDATE products SET stock = stock - ? WHERE id = ?", (quantity, product_id))
        c.execute("INSERT INTO transactions (product_id, type, quantity, total_price) VALUES (?, 'SELL', ?, ?)", (product_id, quantity, total))
        conn.commit()
        print(f"✅ {quantity} পিস মাল বিক্রি হয়েছে। মোট আয়: {total} টাকা")
    else:
        print("❌ পর্যাপ্ত স্টক নেই!")
    conn.close()
