import requests
from bs4 import BeautifulSoup
import os

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

os.makedirs("images", exist_ok=True)

for i, img in enumerate(soup.find_all("img"), start=1):
    img_url = img.get("src")
    if img_url.startswith("http"):
        img_data = requests.get(img_url).content
        with open(f"images/image_{i}.jpg", "wb") as file:
            file.write(img_data)

print("All webpage images downloaded!")