from get_binary import get_binary
from web_gen import web_gen
import requests


apod = "https://api.nasa.gov/planetary/apod"


with open ('cred.cred', 'r') as NASA_API:
    API = NASA_API.readline()

full_url = (str(apod) + "?api_key=" + API)

response = requests.get(full_url)
data = response.json()
#print (data)
header = ("NASA Image of the Day - " + data['title'])
info = data['explanation']
image_url = data['url']
image = (str(data['title']).replace(" ","_") + '.jpg')

get_binary(image_url, image)
web_gen(header, image, info)


