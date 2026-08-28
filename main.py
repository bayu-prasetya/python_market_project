# Harga buah
apple_price = 10_000
orange_price = 15_000
grape_price = 20_000

# Menu input
apple_qty = int(input("Masukan jumlah apel: "))
orange_qty = int(input("Masukan jumlah jeruk: "))
grape_qty = int(input("Masukan jumlah anggur: "))

# Menu detail belanja
total_price_apple = apple_qty * apple_price
total_price_orange = orange_qty * orange_price
total_price_grape = grape_qty * grape_price
total_price = total_price_apple + total_price_orange + total_price_grape

print("\nDetail Belanja\n")
print(f"Apel  : {apple_qty} x {apple_price} = {total_price_apple}")
print(f"Jeruk : {orange_qty} x {orange_price} = {total_price_orange}")
print(f"Anggur: {grape_qty} x {grape_price} = {total_price_grape}")
print(f"\nTotal: {total_price}")