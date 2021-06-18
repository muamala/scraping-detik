import requests

#json_data = requests.get('http://www.floatrates.com/daily/idr.json')

json_data = {'usd': {'code': 'USD', 'alphaCode': 'USD', 'numericCode': '840', 'name': 'U.S. Dollar', 'rate': 6.9588769443092e-05, 'date': 'Thu, 17 Jun 2021 23:55:01 GMT', 'inverseRate': 14370.134836452},
             'eur': {'code': 'EUR', 'alphaCode': 'EUR', 'numericCode': '978', 'name': 'Euro', 'rate': 5.8263550921752e-05, 'date': 'Thu, 17 Jun 2021 23:55:01 GMT', 'inverseRate': 17163.389188946
                     }}

print(json_data)
for data in json_data.values():
    print(data['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])