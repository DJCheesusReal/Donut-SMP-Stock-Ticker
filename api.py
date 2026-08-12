import requests
import json
import ast
import pandas as pd

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