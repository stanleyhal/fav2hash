import requests
import base64
import mmh3

def fav2hash():
	question = input ("Is your favicon located to an URL (1) or on local path (2)?: ")

	if question == "1":
		url=input ("\nInsert the url favicon: ")
		response = requests.get(url)
		convertedData = base64.encodebytes(response.content).decode()
		hash = mmh3.hash(convertedData)
		print("\nHere's your mmh3 hash. Copy/paste this string into Shodan:\nhttp.favicon.hash:",hash)
	elif question == "2":
		localpath=input ("\nPlease insert the local path of the favicon, with the name and the extension:\n")
		with open(localpath, 'rb') as image_file:
			encoded_string = base64.encodebytes(image_file.read())
		hash = mmh3.hash(encoded_string)
		print("\nHere's your mmh3 hash. Copy/paste this string into Shodan:\nhttp.favicon.hash:",hash)
	elif question != "1" or "2":
		print("Wrong choice! Please type the right one\n")
		fav2hash()
fav2hash()
