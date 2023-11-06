user_1 = {"name": "moshe", "bill": 0, "password": 24556}
user_2 = {"name": "ele", "bill": 4000000, "password": 958935}
users = [user_1, user_2]


def get_user_from_list_or_exit(name):
    for user in users:
        if user["name"] == name:
            return user
    print('no user found')
    exit()


def mengr_the_bill(amont, fonkshn, name, ):
    global bill
    print("welcome to my bank")
    fonkshn = int(input("Tap your choice "))
    passbc_1 = int(input("enter your password"))
    for user in users:
        if user["password"] == passbc_1 and user["name"] == name:
            if fonkshn == 1:
                amont = int(input("tap your amount"))
                user = get_user_from_list_or_exit(name)
                user["bill"] += amont
                # bill +=amont
                return user
                if fonkshn == 2:
                    amont = int(input("tap your amount"))
                    user = get_user_from_list_or_exit(name)
                    user["bill"] -= amont

                    return user

                if fonkshn == 3:
                    print("Your balance is", amont)
                if fonkshn == 4:
                    exit()
                else:
                    print('')
        else:
            print("Error")


name = input("enter your name")

print(mengr_the_bill(200, 2, name))
