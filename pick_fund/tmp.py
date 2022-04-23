import requests

header = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/78.0.3904.108 Safari/537.36'}

page = requests.get('https://datacenter-web.eastmoney.com/api/data/v1/get?sortColumns=TRADE_DATE&sortTypes=-1&pageSize=50&pageNumber=3',
                    headers=header)

a='https://datacenter-web.eastmoney.com/api/data/v1/get?callback=jQuery1123013797065092622773_1650636515759&sortColumns=TRADE_DATE&sortTypes=-1&pageSize=50&pageNumber=3&reportName=RPT_VALUEMARKET&columns=ALL&quoteColumns=&filter=(TRADE_DATE%3E%272018-04-22%27)'
print(page)