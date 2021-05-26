import requests
key="155e7051f229ba5506a04b96a6b6ad1bedd20"
url=input("Enter your URL : ")
api_url = f"https://cutt.ly/api/api.php?key={key}&short={url}"
data=requests.get(api_url).json()["url"]
if data["status"]==7:
    print("URL shortened version : ",data["shortLink"])
else:
    print("Some error Occured in shortening : ",data)