from urllib.request import urlopen
import json
from pycbrf.toolbox import ExchangeRates
from datetime import datetime


def get_btc_course():
    url = "https://data.messari.io/api/v1/assets/btc/metrics"
    data = urlopen(url).read().decode('utf-8')
    xz = json.loads(data)
    btc_course = xz["data"]["market_data"]["price_usd"]
    return btc_course


def get_usd_course():
    rates = ExchangeRates(str(datetime.now().date()))
    usd_course = rates["USD"].value
    return float(usd_course)


def get_btc_in_roubles():
    btc = get_btc_course()
    usd = get_usd_course()
    return btc * float(usd)


def calculate(x):
    return get_btc_course() * get_usd_course() * x


def main():
    btc_course = get_btc_course()
    usd_course = get_usd_course()
    print(f"Курс биткоина к американскому доллару: {btc_course}")
    print(f"Курс американского доллара к рублю: {usd_course}")
    print(f"Курс биткоина к рублю: {get_btc_in_roubles()}")


if __name__ == "__main__":
    main()
