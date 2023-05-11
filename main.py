import requests
from send_api_to_email import send_email

topic = "tesla"
api_key = "fcbbd2d228124532a6aa0b367d17cf2d"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-04-11&" \
      "sortBy=publishedAt&" \
      "apiKey=fcbbd2d228124532a6aa0b367d17cf2d&" \
      "language=en"

# request
req = requests.get(url)
# we get a dict
content = req.json()

# access the article titles and description
message = ""
for article in content["articles"][:10]:
    if article['title'] is not None:
        message = "Subject: Today's News" +\
                  "\n" + message \
                  + article['title'] \
                  + "\n" \
                  + article['description'] \
                  + "\n" \
                  + article['url']\
                  + 2*"\n"

message = message.encode("utf-8")
send_email(message)
