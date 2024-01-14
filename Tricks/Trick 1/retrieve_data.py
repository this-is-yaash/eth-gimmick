import requests
url = "www.google.com" #any url as per your need
response = requests.get(url)
print(response.text)