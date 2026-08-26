import requests
import io
from PIL import Image

user = str(input("Who's head to request: "))
response = requests.get(f"https://api.mcheads.org/head/{user}/32")
print(response.content)

image_data = io.BytesIO(response.content)
img = Image.open(image_data)
img.show()
