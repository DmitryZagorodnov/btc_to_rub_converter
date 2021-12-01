from urllib.request import urlopen
import json
from pycbrf.toolbox import ExchangeRates
from datetime import datetime


url = "https://data.messari.io/api/v1/assets/btc/metrics"
data = urlopen(url).read().decode('utf-8')
xz = json.loads(data)
btc_course = xz["data"]["market_data"]["price_usd"]
print(f"Курс биткоина к американскому доллару: {btc_course}")

rates = ExchangeRates(str(datetime.now().date()))
usd_course = rates["USD"].value
print(f"Курс американского доллара к рублю: {usd_course}")

print(f"Курс биткоина к рублю: {btc_course * float(usd_course)}")

num = input("Введите количество биткоинов: ")
print(f"{btc_course * float(usd_course) * float(num)} руб.")