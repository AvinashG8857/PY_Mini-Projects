import requests
from bs4 import BeautifulSoup


all_quotes= []

for page in range(1,6):
    url= f"http://quotes.toscrape.com/page/{page}/"
    response= requests.get(url)
    soup= BeautifulSoup(response.text, "html.parser")
    # print(soup)
    quotes= soup.find_all("span",class_="text")
    # print(quotes.pretif)
    authors= soup.find_all("small",class_= "author")

    for quote,author in zip(quotes,authors):
        all_quotes.append({"quote": quote.text,"author":author.text})

print(f"\n Collected {len(all_quotes)} quotes")

for item in all_quotes[:5]:
    print(item)
    print()