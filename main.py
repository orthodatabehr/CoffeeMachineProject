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


# Turn off the coffee machine with 'off' command --> exits program
# if user input is 'off' then will exit while loop

# Print Report - display resources dictionary
def display_report():
    """This function will return a string with the current ingredient status and amount of user funds."""
    water = 'Water: ' + str(resources['water']) + 'ml'
    milk = 'Milk: ' + str(resources['milk']) + 'ml'
    coffee = 'Coffee: ' + str(resources['coffee']) + 'g'
    money = 'Money: $' + str(profit)
    return f'{water}\n{milk}\n{coffee}\n{money}'


# Check resources to see if sufficient - all resources must be sufficient for drink to be made
def check_resources(drink):
    """This function will check to see if current ingredients are sufficient to make the drink requested."""
    if resources["water"] < MENU[drink]["ingredients"]["water"]:
        return 'water'
    elif resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
        return 'coffee'
    elif drink != 'espresso' and resources["milk"] < MENU[drink]["ingredients"]["milk"]:
        return 'milk'
    else:
        return 'All good. The should not see this message'


def compute_coins(q, d, n, p):
    """This function returns float value of total user funds."""
    total = round(q * 0.25 + d * 0.1 + n * 0.05 + p * 0.01, 2)
    return total


def process_funds(funds, drink):
    """This function will compare the user funds and price of drink to determine if enough money is inserted."""
    if MENU[drink]["cost"] > funds:
        return False
    else:
        return True


def make_drink(drink):
    """This function will simulate making the drink by deducting the chosen drink's ingredients from resources."""
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    if drink != 'espresso':
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    return f'Here is your {drink}. Enjoy!'


# After creating the functions, the final part is to incorporate UDF for range of commands
# Commands: off, report, latte, espresso, latte, cappuccino
machine_on = True
profit = 0
while machine_on:
    # Prompt for the user
    user_order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_order == 'off':
        machine_on = False
    elif user_order == 'report':
        print(display_report())
    elif user_order in ['latte', 'cappuccino', 'espresso']:
        deficiency = check_resources(user_order)
        if deficiency not in ['coffee', 'milk', 'water']:
            # Process Coins - take input of coins by type of American coin and compute total user funds.
            print('Please insert coins.')
            quarters = float(input('How many quarters?: '))
            dimes = float(input('How many dimes?: '))
            nickels = float(input('How many nickels?: '))
            pennies = float(input('How many pennies?: '))
            user_funds = compute_coins(quarters, dimes, nickels, pennies)
            if process_funds(user_funds, user_order):
                for item in MENU:
                    if user_order == item:
                        change = round(user_funds - MENU[item]['cost'], 2)
                        profit += MENU[item]['cost']
                        print(f"Here is ${change} in change.")
                        print(make_drink(item))
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(f'Sorry there is not enough {deficiency}.')
    else:
        print("Please choose one of the drink options or choose 'Report' or turn 'off'.")
