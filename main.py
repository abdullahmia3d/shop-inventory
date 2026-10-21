from database import init_db
from services import add_product, purchase_stock, sell_product

def main():
    init_db()
    while True:
        print("\n--- 🏪 দোকানের হিসাব ---")
        print("1. নতুন প্রোডাক্ট যোগ করুন")
        print("2. মাল কিনুন (স্টক যোগ)")
        print("3. মাল বিক্রি করুন")
        print("0. বেরিয়ে যান")
        
        choice = input("আপনার পছন্দ: ")
        
        if choice == '1':
            name = input("প্রোডাক্টের নাম: ")
            buy = float(input("কেনার দাম: "))
            sell = float(input("বিক্রির দাম: "))
            add_product(name, buy, sell)
        elif choice == '2':
            pid = int(input("প্রোডাক্ট আইডি: "))
            qty = int(input("কত পিস: "))
            price = float(input("প্রতি পিসের দাম: "))
            purchase_stock(pid, qty, price)
        elif choice == '3':
            pid = int(input("প্রোডাক্ট আইডি: "))
            qty = int(input("কত পিস: "))
            sell_product(pid, qty)
        elif choice == '0':
            break
        else:
            print("ভুল পছন্দ!")

if __name__ == "__main__":
    main()
