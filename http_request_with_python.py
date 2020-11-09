#import a library that allows to make a http request
import requests
#setting the api endpoint
url="https://www.metaweather.com/api/location/search/?query=san"
#using the library to perfrom an http get requests to the url
response=requests.get(url)
#print out the data of response
print(response.text)