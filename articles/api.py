import requests


def get_data(article):
    url = 'http://api.ipstack.com/{}?access_key={}'
    key = 'b49fc28743af67723f7f03174fca0f52'
    return [
        requests.get(url.format(ip, key)).json()
        for ip in article.body_as_list
    ]
