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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



def solicitar_pago():
    print("Please instert coins")
    quarter = int(input("How many quarters?"))*0.25
    dimes = int(input("How many dimes?"))*0.1
    nickels = int(input("How many nickel?"))* 0.05
    pennies = int(input("How many pennies?"))*0.01
    pay = round(quarter+dimes+nickels+pennies,2)
    return pay

def report():
    for key,value in resources.items():
        print(f"{key}: {value}")
    print(f"${profit}")

def check_resourses(answer):
    if MENU[answer]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water.")
        return False
    elif MENU[answer]["ingredients"]["coffee"]> resources["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    if answer != "espresso":
        if MENU[answer]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry there is not enough milk.")
            return False
    return True

def check_pay(pay,answer):
    if pay >= MENU[answer]["cost"]:
        change = pay - MENU[answer]["cost"]
        print(f"Here is ${change} in change.")
        update_resourses(answer)
        print(f"Here is your {answer}. Enjoy!")
        return True
    else:
        print(f"Sorry that's not enough money. Money refunded because {answer} cost is ${MENU[answer]['cost']}")
        return False

def update_resourses(answer):
    resources["water"] = resources["water"] - MENU[answer]["ingredients"]["water"]
    resources["coffee"] = resources["coffee"] - MENU[answer]["ingredients"]["coffee"]
    if answer != "espresso":
        resources["milk"] = resources["milk"] - MENU[answer]["ingredients"]["milk"]
    global profit
    profit += MENU[answer]["cost"]


turn_on =True
while turn_on:
    answer = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if answer == "report":
        report()
    elif answer == "turn off":
        turn_on = False
    else:
        if check_resourses(answer) == True:
            pay = solicitar_pago()
            print(pay)
            check_pay(pay,answer)



