import requests
url1 = 'http://suninatas.com/challenge/web04/web04_ck.asp'
url2 = 'http://suninatas.com/challenge/web04/web04.asp'

ss = requests.Session()
ss.headers['User-Agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:72.0) Gecko/20100101 SuNiNaTaS"
for i in range(0,50) :
    ss.post(url1)

response = ss.post(url2)
print(response.text)
