import json

with open("data.json") as data:
    users = json.loads(data.read())


def get_user_from_list_or_none(name):
    for user in users:
        if user["name"] == name:
            return user
    return None


def save_users_data():
    data_json = json.dumps(users)
    with open("data.json", "w") as data:
        data.write(data_json)


def login(username, password):
    user = get_user_from_list_or_none(username)  # {name: moshe, password:123456, balance:300} \ None

    if user["password"] == password:
        return user
    else:
        return None


def bank_manager(amount, function, name):
    user = get_user_from_list_or_none(name)

    if function == 1:
        user["bill"] += amount
        save_users_data()
        return user

    if function == 2:
        user["bill"] -= amount
        save_users_data()
        return user

    if function == 3:
        return user["bill"]
