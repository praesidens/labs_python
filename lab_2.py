import requests
from requests_html import HTMLSession


url = "http://dfedorov.spb.ru/python3/src/romeo.txt"

r = requests.get(url)
print(r.text)

req = requests.get("http://dfedorov.spb.ru/python/files/tutchev.txt")
print(req.text)
