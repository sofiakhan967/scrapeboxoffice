import pyshorteners
url= input(" Enter your URL : ")
print("your url : " ,pyshorteners.Shortener().tinyurl.short(url))