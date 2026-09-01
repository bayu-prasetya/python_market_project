# Daftar Harga buah
fruit_list = [
    # product_name, price, stock
    ["apple", 10_000, 10], # 0
    ["orange", 15_000, 10], # 1
    ["grape", 20_000, 10] # 2
]

# Menu detail belanja
price_per_fruit = []
qty_per_fruit = []
total_price = 0
for fruit in fruit_list:
    qty = int(input(f"Masukan jumlah {fruit[0]}"))
    price = qty * fruit[1]
    price_per_fruit.append(price)
    qty_per_fruit.append(qty)
    total_price += price

print("\nDetail Belanja\n")
print(f"Apel  : {qty_per_fruit[0]} x {fruit_list[0][1]} = {price_per_fruit[0]}")
print(f"Jeruk : {qty_per_fruit[1]} x {fruit_list[1][1]} = {price_per_fruit[1]}")
print(f"Anggur: {qty_per_fruit[2]} x {fruit_list[2][1]} = {price_per_fruit[2]}")
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