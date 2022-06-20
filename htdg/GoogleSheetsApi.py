from pprint import pprint
from datetime import datetime
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
from django import db
from .models import Orders
from .parser import dollor

# Файл, полученный в Google Developer Console
CREDENTIALS_FILE = 'credentials.json'
# ID Google Sheets документа (можно взять из его URL)
spreadsheet_id = '12nl-lf9m5i5ROq_CsxdITq41039hHrsy4iChgOD37vY'

# Авторизуемся и получаем service — экземпляр доступа к API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

# Пример чтения файла
values = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range='A2:D51',
    majorDimension='ROWS'
).execute()


def add_db():
    for i in values['values'] :
        price = i[2]
        pr = float(price)
        price_rub = pr * dollor
        id_ = i[0]
        number = i[1]
        dete = i[3]
        dete = str(dete)
        a = Orders(id=id_,namber=number,price=price,price_rub=price_rub,date=dete)
        a.save()
    
    
    
