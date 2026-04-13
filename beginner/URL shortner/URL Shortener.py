import pyshorteners

def shorten_url(url):
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(url)   # using TinyURL service
    return short_url

print("=== URL Shortener ===")
url = input("Enter the URL to shorten: ")
short = shorten_url(url)
print("Shortened URL:", short)