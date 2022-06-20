import requests

from bs4 import BeautifulSoup as BS
# получаем данные об курсах валют
r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp?date_req=02/03/2002')
html = BS(r.content,'xml')
# фильтруем данные и получаем отношение рубль доллор 
# не знаю почему но данные с сайта не соотвествуют действительности
for i in html.findAll(ID="R01235"):
    value = i.findAll('Value')
    value1=value[0].text
    s = value1.replace(",",".")
    dollor = float(s)