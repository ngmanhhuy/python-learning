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

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

def refill_resources():
    resources['water'] = 300
    resources['milk'] = 200
    resources['coffee'] = 100
    print("Resources refilled!")

def is_enough_resources(drink):
    enough_resource = True
    drink_ingredients = MENU[drink]['ingredients']
    for ingredient in drink_ingredients:
        if resources[ingredient] < drink_ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}. Required extra {drink_ingredients[ingredient] - resources[ingredient]}")
            enough_resource = False
    return enough_resource

def is_process_coin_successful(drink):
    cost = MENU[drink]['cost']
    total = 0
    global money
    print("Please insert coins.")
    quarters = float(input("Quarters: "))
    dimes = float(input("Dimes: "))
    nickles = float(input("Nickles: "))
    pennies = float(input("Pennies: "))

    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01

    if total < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif total > cost:
        print(f"Here is ${total - cost:.2f} dollars in change.")
        money += cost
        return True
    else:
        money += cost
        return True

def make_coffee(drink):
    ingredients = MENU[drink]['ingredients']
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
    print(f"Here is your {drink}. Enjoy!")

money = 0
def coffee_machine():
    off_machine = False
    while not off_machine:
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
        match user_input:
            case "off":
                off_machine = True
            case "report":
                print_report()
            case "refill":
                refill_resources()
            case _ if user_input in MENU:
                if is_enough_resources(user_input) and is_process_coin_successful(user_input):
                    make_coffee(user_input)
            case _:
                print("Invalid input! Please try again.")

coffee_machine()
