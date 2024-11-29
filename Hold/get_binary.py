import requests

''' 
This is how you get a file like a 
jpg or other binary file.
'''
def get_binary(url, pic):

    binary = requests.get(url)
    filename = pic
    #filename = str(url).split("/")[-1]

    with open (filename, "wb") as file:
        file.write(binary.content)

if __name__ == "__main__":
    url = "https://services.swpc.noaa.gov/images/animations/ovation/north/latest.jpg"
    get_binary(url)