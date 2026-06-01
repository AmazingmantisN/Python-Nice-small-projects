from idlelib.debugger_r import restart_subprocess_debugger

import data as d
import random as r


data = d.MENU
resource = d.resources



def resource_checker(r, dat, userwant):
    list = ["milk", "water", "coffee"]
    if userwant == "espresso":
        list.remove("milk")
    enough = True
    for i in list:

        if r[i] < dat[userwant]["ingredients"][i]:
            print(f"Sorry there isnt enough {i}!\n")
            enough = False
            break
    if enough == True:
        for i in list:
            r[i] -= dat[userwant]["ingredients"][i]
    return enough

def money_processing(d, k):
    listt = {"quarters" : 0.25, "dimes": 0.1, "nickles": 0.05, "pennies" : 0.01}
    total = 0
    enough = True
    for i in listt:
        total += (int(input(f"How many {i}?\n")) * listt[i])
    if total < d[k]["cost"]:
        print(f"Not enough money\n")
        enough = False

    return enough



running = True

while running == True:
    print("\n" * 50)
    print("Hi welcome to the coffee machine\n")
    user_answer = input("What would you like? (espresso/cappuccino/latte)")
    if user_answer == "report":
        print(f"Water: {resource["water"]}\n")
        print(f"Milk: {resource["milk"]}\n")
        print(f"Coffee: {resource["coffee"]}\n")
    elif user_answer == "off":
        running = False

    else:
        if resource_checker(resource, data, user_answer):
            if money_processing(data, user_answer):
                print(f"Enjoy your {user_answer}")
                print("\n" * 50)





