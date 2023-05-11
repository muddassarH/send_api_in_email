import requests
import streamlit as st

topic = "tesla"
image = "https://api.nasa.gov/assets/img/general/apod.jpg"
api_key = "HDOs1RZT5Sg93o50xBlfUY72BBJGFwt2bcwif7Vp"
url = f"https://api.nasa.gov/planetary/apod?" \
      f"api_key={api_key}"


response1 = requests.get(url)
data = response1.json()
title = data['title']
image_url = data['url']
explanation = data['explanation']

image_filepath = "img.png"

response2 = requests.get(image_url)
with open(image_filepath, 'wb')as file:
    file.write(response2.content)

st.title(title)
st.image(image_filepath)
st.write(explanation)
