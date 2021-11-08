import task_4_2
import task_4_3

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
currency = input("Введите имя валюты: ")


task_4_2.currency_rates(url, currency)
task_4_3.currency_rates(url, currency)