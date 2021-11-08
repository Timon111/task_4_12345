import requests

from requests import get, utils
url = 'http://www.cbr.ru/scripts/XML_daily.asp'
currency = input("Введите имя валюты: ")


def currency_rates(url, currency):
    response = get(url)
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    c_len = len(content)
    status_code = response.status_code
    if currency in content and status_code == 200:
        cur_ind = int(content.index(currency))
        sli = content[cur_ind:c_len]
        sli_len = len(sli)
        beg = int(sli.index("<Value>") + (c_len-sli_len) + 7)
        end = int(sli.index("</Value>")+ (c_len-sli_len))
        print(content[beg:end])
    else:
        print("No currency such thin in file")


currency_rates(url, currency)
    #currency_rates(url, "USd")
    #71.7846
