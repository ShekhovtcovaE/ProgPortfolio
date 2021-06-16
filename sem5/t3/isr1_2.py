from xml.etree import ElementTree as ET
from urllib.request import urlopen


def singleton(cls):
    instances = {}
    def getinstance(*args):
        if cls not in instances:
            instances[cls] = cls(*args)
        return instances[cls]
    return getinstance


@singleton
def get_currencies(currencies_ids_lst=None):
    result = {}
    d = input('Enter date ')
    m = input('Enter month ')
    y = input('Enter year ')
    res = urlopen("http://www.cbr.ru/scripts/XML_daily.asp?date_req=" + d + '/' + m + '/' + y)
    root = ET.parse(res).getroot()
    list_of_val = root.findall('Valute')
    for i in list_of_val:
        #if str(valute_id) in currencies_ids_lst:
        val = i.find('Value').text
        name = i.find('Name').text
        result[i.find('NumCode').text] = (name, val)
    print(result)

get_currencies()
