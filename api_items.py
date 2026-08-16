import requests
import json
import ast
import pandas as pd
import matplotlib.pyplot as plt

item_name = str(input("Enter item to search:"))
u_item_name =  item_name.replace(" ", "_")

df = pd.read_csv("donut_items.csv")

matches = df[df["itemName"].str.contains(u_item_name, case=False, na=False)]
num_matches = len(matches)
if num_matches ==0:
    print("No matches found")
    exit()
elif num_matches ==1:
    print("Found item!")
    selected_item = matches.iloc[0]
    stack = matches["stackSize"]
else:
    print("Multiple matches found:")
    for index, name in enumerate(matches["itemName"]):
        print(f"{index + 1}. {name}")
    
    choice = int(input("Enter the number of the item you want to select: "))
    selected_item = matches.iloc[choice - 1]

item_id = str(selected_item["id"])
stack = selected_item["stackSize"]
item_name = selected_item["itemName"]
display_name = selected_item["itemName"].replace("_", " ")

print("1: Current Price")
print("2: Last 24 hours")
data_length = int(input())

match data_length:
    case 1:
        response = requests.get("https://api.donut.auction/v2/items/prices?itemIds=" + item_id)

        parsed = json.loads(response.text)
        price = parsed[0]['price']
        value = price['value']

        if value > 1000000: 
            value = value / 1000000
            value = round(value, 2)
            print(f"{display_name} cost: ${value}M for {stack} items")
        elif value > 1000:
            value = value / 1000
            value = round(value, 2)
            print(f"{display_name} cost: ${value}K for {stack} items")
        elif value < 1000:
            value = round(value, 2)
            print(f"{display_name} cost: ${value} for {stack} items")
    case 2:
        response = requests.get(f"https://api.donut.auction/v2/items/{item_id}/prices?period=1d")
        parsed = json.loads(response.text)
        print(parsed)
        prices = [point['avgPrice'] for point in parsed['auctionPricePoints']]
        df = pd.DataFrame({
            'Time': parsed['buckets'],
            'Price': prices
        })
        df['Price'] = df['Price'].ffill()
        df['Price'] = df['Price'] / 1000000
        df['Time'] = pd.to_datetime(df['Time'])
        plt.plot(df['Time'], df['Price'], color='blue')
        plt.title("Last 24 hours")
        plt.xlabel("Time")
        plt.ylabel("Price (M)")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.show()