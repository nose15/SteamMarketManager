from src.steamAPIwrapper import inventoryMethods, marketMethods


def get_user_inventory(user_id: str, app_id: int) -> dict:
    count = inventoryMethods.get_inventory_count(user_id, app_id)
    data = inventoryMethods.get_inventory_data(user_id, app_id, count)
    formatted_data = inventoryMethods.format_inventory_data(data)

    return formatted_data


def get_item_listing_price(app_id: int, currency_code: int, item_market_hash_name: str):
    marketMethods.get_current_price(app_id, currency_code, item_market_hash_name)
