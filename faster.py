import requests

url = "http://suninatas.com/challenge/web07/web07.asp"
url2 = "http://suninatas.com/challenge/web07/web07_1.asp"

s = requests.Session()
s.post(url)
req = s.post(url2)
print(req.text)
