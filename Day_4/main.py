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
        "cost": 3.0
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

amount = {
    "money": 0
}

def Welcome():
    drink = input("Hi\nWhat would you like to drink? (Espresso/Latte/Cappuccino)")
    return drink

def print_report():
    print('Current Resources are:\n')
    for resource, value in resources.items():
        print(resource, ":", value)

def check_resources_sufficient(drink):
    sufficient_amount = {}
    for ingredient, amount in MENU[drink]["ingredients"].items():
        for resource, value in resources.items():
            if resource == ingredient and value > amount:
                sufficient_amount[resource] = True
            elif resource == ingredient and value < amount:
                sufficient_amount[resource] = False

    if all(value == True for value in sufficient_amount.values()):
        return True
    else:
        return False

def process_coins(drink):
    print("That will be {:.2f}".format(MENU[drink]["cost"]))
    print("Please insert your coins")
    quarters = float(input("quarter: "))
    dimes = float(input("Dimes: "))
    nickles = float(input("nickles: "))
    pennies = float(input("pennies: "))
    total_amount = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)                

    if MENU[drink]["cost"] > total_amount:
        print("Amount inserted: {:.2f}" .format(total_amount))
        return False
    else:
        print("Amount inserted: {:.2f}" .format(total_amount))
        change = total_amount - MENU[drink]["cost"]
        print("Your change is {:.2f}" .format(change))
        amount["money"] = MENU[drink]["cost"]
        
        return True 

def make_a_coffee(drink):
    for resource in resources:
        if resource in MENU[drink]["ingredients"]:
            resources[resource]  = resources[resource] - MENU[drink]["ingredients"][resource]
            # print(resources[resource], MENU[drink]["ingredients"][resource]   )
    print("Thank you for coming, your {} is ready!".format(drink))

if __name__ =="__main__":

    state = 'on'
    while state != 'off':
        drink = Welcome() 
        if drink == 'off':
            state = 'off'
            break
        if drink != 'cappuccino' or drink != 'espresso' or drink != 'latte':
            print("Sorry, I did not understand that, could you please reenter your drinks name")
            drink = Welcome()
            pass
        if check_resources_sufficient(drink):
            if process_coins(drink):
                print("Sufficient funds.\nPlease standby while we prepare your order.")
                print(".")
                print(".")
                print(".")
                make_a_coffee(drink)
            else:
                print("Insufficient funds.\nRefunding money...")
        else:
            print("Sorry, we do not have enough resources at the moment to process your order.\nPlease try again later.")
   
