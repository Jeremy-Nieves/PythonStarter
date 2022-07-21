prices = {
    'arugala': 1.10,
    'basil': 2.54,
    'blackberries': 4.93,
    'blueberries': 2.88,
    'coconut': 7.15,
    'fennel': 3.36

}

prices["orange"] = 1.69

product = input("What product are you buying?")
price = prices.get(product)
if price:
    print(f"{product} is ${price}")
else:
    print("I don't have that in stock!")

del prices["basil"]
print(prices)

# ski_runs = {"easy": "green", "intermediate": "blue", "advanced": "black"}
# ski_runs.get("expert")
# print(ski_runs)
# 
# ski_runs = {"easy": "green", "intermediate": "blue", "advanced": "black"}
# "blue" in ski_runs
# ski_runs.pop("easy")
# print(ski_runs)

