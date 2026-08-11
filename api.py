import requests
import json
import ast
item = "c4c7f62a-d21a-4e94-b6a3-355a15349705"
response = requests.get("https://api.donut.auction/v2/items/prices?itemIds=" + item)

parsed = json.loads(response.text)
price = parsed[0]['price']
value = price['value']
print(f"Elytra cost: ${value}")
if value > 1000000:
    value = value / 1000000
    value = round(value, 2)
    print(f"Elytra cost: ${value}M")