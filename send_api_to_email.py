import smtplib
import ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "muddassarhussain90@gmail.com"
    password = os.environ["PASSWORD"]
    receiver_email = "muddassarhussain90@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver_email, message)
