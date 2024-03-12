menu = ["coffee","tea","sandwich","cake"]

stock = { "coffee": 68,
          "tea": 42,
          "sandwich": 39,
          "cake": 26
        }

price = { "coffee": 2.50,
          "tea": 2.00,
          "sandwich": 3.00,
          "cake": 2.75
        }

total_stock = 0

for item in menu:
    item_total = stock[item] * price[item]
    total_stock += item_total

print(total_stock)
