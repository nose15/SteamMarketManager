from requests import get
import json


def get_current_price(app_id, currency, item_market_hash_name):
    url = f"http://steamcommunity.com/market/priceoverview/?appid={app_id}&currency={currency}&market_hash_name={item_market_hash_name}"
    response = get(url)
    data = response.json()
    return data['lowest_price']


