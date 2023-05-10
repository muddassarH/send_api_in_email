import requests

from send_api_to_email import send_email

api_key = "fcbbd2d228124532a6aa0b367d17cf2d"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-04-09&sortBy=publishedAt&" \
      "apiKey=fcbbd2d228124532a6aa0b367d17cf2d"

# request
req = requests.get(url)
# we get a dict
content = req.json()
# access the article titles ans decription
message =""
for article in content['articles']:
    if article['title'] is not None:
        message = message + article['title'] + "\n" + article['description'] + 2*"\n"

message = message.encode("utf-8")
send_email(message)
