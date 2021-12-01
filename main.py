from urllib.request import urlopen
import json


url = "https://data.messari.io/api/v1/assets/btc/metrics"
data = urlopen(url).read().decode('utf-8')
xz = json.loads(data)
btc_course = xz["data"]["market_data"]["price_usd"]
print(f"Курс биткоина к американскому доллару: {btc_course}")