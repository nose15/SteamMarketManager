from steamAPIwrapper.steamAPI import get_user_inventory


def main():
    app_id = 730    # CS:GO
    currency_code = 6   # PLN

    inventory = get_user_inventory("76561198151374664", app_id)
    print(inventory)


if __name__ == '__main__':
    main()

