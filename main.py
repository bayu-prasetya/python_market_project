# Daftar Harga buah
fruit_list = [
    # product_name, price, stock
    {"product_name": "apple", "product_price": 10_000, "product_stock": 10},
    {"product_name": "orange", "product_price": 20_000, "product_stock": 10},
    {"product_name": "grape", "product_price": 25_000, "product_stock": 10}
]

# Menu input
apple_qty = int(input("Masukan jumlah apel: "))
orange_qty = int(input("Masukan jumlah jeruk: "))
grape_qty = int(input("Masukan jumlah anggur: "))

# Menu detail belanja
total_price_apple = apple_qty * fruit_list[0]["product_price"]
total_price_orange = orange_qty * fruit_list[1]["product_price"]
total_price_grape = grape_qty * fruit_list[2]["product_price"]
total_price = total_price_apple + total_price_orange + total_price_grape

print("\nDetail Belanja\n")
print(f"Apel  : {apple_qty} x {fruit_list[0]["product_price"]} = {total_price_apple}")
print(f"Jeruk : {orange_qty} x {fruit_list[1]["product_price"]} = {total_price_orange}")
print(f"Anggur: {grape_qty} x {fruit_list[2]["product_price"]} = {total_price_grape}")
print(f"\nTotal: {total_price}")

# payment feature
print("-"*20) # dekorasi pembatas
payment = int(input("\nMasukan jumlah uang: "))
selisih = total_price - payment
if payment < total_price:
    print("\n[X] Transaksi dibatalkan !")
    print(f"Uang kurang sebesar {selisih}")
else:
    print("\nTerima kasih!")
    if selisih:
        print(f"\nUang kembalian anda: {abs(selisih)}")