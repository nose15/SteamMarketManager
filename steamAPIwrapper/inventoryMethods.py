from requests import get
import json


"""
For now these methods don't actually call the api because the data formatting and processing features are still in 
development. They just return data from dummy files which simulate the output of an API call.
"""


def get_inventory_count(user_id, app_id):
    url = f"http://steamcommunity.com/inventory/{user_id}/{app_id}/" \
          f"2?l=english&count=1"

    count = 0

    with open("steamAPIwrapper/exampleFiles/exampleCountRead.json", "r") as f:
        line = f.read()
        data_dict = json.loads(line)
        count = data_dict["total_inventory_count"]

    return count


def get_inventory_data(user_id, app_id, count):
    url = f"http://steamcommunity.com/inventory/{user_id}/{app_id}/" \
          f"2?l=english&count={count}"

    with open("steamAPIwrapper/exampleFiles/exampleInventoryDownload.json", "r", encoding="utf8") as f:
        lines = f.read()
        data_dict = json.loads(lines)

    return data_dict


def format_inventory_data(data: dict):
    formatted_data = {}

    for description in data["descriptions"]:
        if description['marketable'] == 1:
            formatted_data[description['classid']] = {'name': description['market_hash_name'], 'amount': 0}

    for asset in data["assets"]:
        if asset["classid"] in formatted_data.keys():
            formatted_data[asset["classid"]]['amount'] += 1

    return formatted_data
