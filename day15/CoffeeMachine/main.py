MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

MONEY = 0 

def validate_input(coins_input):
    try:
        coins = int(coins_input)
    except ValueError:
        print("Invalid input. Please ienter a number")
    return coins

def transaction(order):
    print("please insert coins.")
    quarters = input("how many quarters?: ")
    quarters_value = validate_input(quarters) * 25
    dimes = input("how many dimes?: ")
    dimes_value = validate_input(dimes) * 10
    nickles = input("how many nickles?: ")
    nickles_value = validate_input(nickles) * 5
    pennies = input("how many pennies?: ")
    pennies_value = validate_input(pennies) * 1
    total_value = quarters_value + dimes_value + nickles_value + pennies_value

    if total_value >= MENU[order]["cost"] * 100:
        change = total_value - MENU[order]["cost"] * 100
        print(f"Here is ${change / 100} in change.")
        print(f"Here is your {order}. Enjoy!")
        global MONEY
        MONEY += MENU[order]["cost"]
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def manage_resources(order):
    global resources
    global MENU

    for ingredient in MENU[order]["ingredients"]:
        if ingredient in resources:
            # Subtract only if the ingredient is required for the order
            resources[ingredient] -= MENU[order]["ingredients"][ingredient]
        else:
            print(f"Error: {ingredient} is not a valid resource.")
            return


# espresso does not need milk as ingrediencts. so check if the ingredients in the MENU first before validation
def validate_resources(order):
    global resources
    global MENU

    if order not in MENU:
        print("Sorry, that's not a valid order.")
        return False

    for ingredient in MENU[order]["ingredients"]:
        if ingredient in resources:
            if resources[ingredient] < MENU[order]["ingredients"][ingredient]:
                print(f"Sorry there is not enough {ingredient}")
                return False
        else:
            print(f"Sorry, we do not have {ingredient}")
            return False

    return True


def print_resources():
    available_water = resources["water"]
    print(f"Water: {available_water}")
    available_milk = resources["milk"]
    print(f"MilK: {available_milk}")
    available_coffee = resources["coffee"]
    print(f"Coffee: {available_coffee}")
    global MONEY
    print(f"Money: {MONEY}")
    return

while True:

    order = input(" What would you like? (espresso/latte/cappuccino): ")

    if order in MENU:
        if validate_resources(order=order):
            transaction(order=order)
            manage_resources(order=order)
    elif order == "report":
        print_resources()
    else:
        print("that is not in the MENU. Please select order again.")