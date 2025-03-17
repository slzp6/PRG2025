""" p2_13.py """

fruits = [["apple", 386, 14.0], ["banana", 286, 11.0],
          ["cranberry", 8086, 9.0]]
fruits_qty = sorted(fruits, key=lambda x: x[1])
fruits_price = sorted(fruits, key=lambda x: x[2])

print("fruits:", fruits)
print("qty:   ", fruits_qty)
print("price: ", fruits_price)
