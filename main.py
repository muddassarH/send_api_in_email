import requests

api_key = "fcbbd2d228124532a6aa0b367d17cf2d"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-04-09&sortBy=publishedAt&" \
      "apiKey=fcbbd2d228124532a6aa0b367d17cf2d"

# request
req = requests.get(url)
# we get a dict
content = req.json()
# access the article titles ans decription
for article in content['articles']:
    print(article['title'])
