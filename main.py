def report(w,c,m,cash):
    print(f"Water: {w}ml\nMilk: {m}ml\nCoffee: {c}g\nMoney: ${cash}")

def choose():
    select=input("What would you like? (espresso/latte/cappuccino): ").lower()
    if select=='report':
        return 1
    elif select=='off':
        return 2
    else:
        return select

def error(selection,lst):
    w=lst['water']
    c=lst['coffee']
    m=lst['milk']
    if selection == "espresso":
        if w < 50 and c < 18:
            print("Sorry there is not enough water and coffee.")
        if w < 50:
            print("Sorry there is not enough water.")
        else:
            print("Sorry there is not enough coffee.")
    elif selection=="latte":
        if w < 50 and c < 24 and m < 100:
            print("Sorry there is not enough water, coffee and milk.")
        elif w < 50 and c < 24:
            print("Sorry there is not enough water and coffee.")
        elif w < 50 and m < 100:
            print("Sorry there is not enough water and milk.")
        elif m < 100 and c < 24:
            print("Sorry there is not enough milk and coffee.")
        elif w < 200:
            print("Sorry there is not enough water.")
        elif c < 24:
            print("Sorry there is not enough coffee.")
        else:
            print("Sorry there is not enough milk.")
    elif selection=="cappuccino":
        if w < 250 and c < 24 and m < 150:
            print("Sorry there is not enough water, coffee and milk.")
        elif w < 250 and c < 24:
            print("Sorry there is not enough water and coffee.")
        elif w < 250 and m < 150:
            print("Sorry there is not enough water and milk.")
        elif m < 150 and c < 24:
            print("Sorry there is not enough milk and coffee.")
        if w < 250:
            print("Sorry there is not enough water.")
        elif c < 24:
            print("Sorry there is not enough coffee.")
        else:
            print("Sorry there is not enough milk.")

def check_ingredient(selection, lst):
    if selection=="espresso" and lst['water']>=50 and lst['coffee']>=18:
        return 1
    elif selection=="latte" and lst['water']>=200 and lst['coffee']>=24 and lst['milk']>=100:
        return 1
    elif selection=="cappuccino" and lst['water']>=250 and lst['coffee']>=24 and lst['milk']>=150:
        return 1
    else:
        return 0

def handle_cash():
    print("Please insert coins.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    t_money = (.25*quarters)+(.10*dimes)+(0.05*nickles)+(0.01*pennies)
    return t_money

def transaction(selection,money_inserted,lst):
    if selection=="espresso":
        if money_inserted>=1.5:
            print(f"Here is ${round(money_inserted-1.5,2)} dollars in change.")
            print(f"Your {selection} is being dispensed. Enjoy!")
            lst['water'] -= 50
            lst['coffee'] -= 18
            lst['money'] += 1.5
        else:
            print(f"Not enough money inserted!. ${money_inserted} refunded!")
    elif selection == "latte":
            if money_inserted >= 2.5:
                print(f"Here is ${round(money_inserted - 2.5,2)} dollars in change.")
                print(f"Your {selection} is being dispensed. Enjoy!")
                lst['water'] -= 200
                lst['coffee'] -= 18
                lst['milk'] -= 100
                lst['money'] += 2.5
            else:
                print(f"Not enough money inserted. ${money_inserted} refunded!")
    elif selection == "cappuccino":
            if money_inserted >= 3.0:
                print(f"Here is ${round(money_inserted - 3.0,2)} dollars in change.")
                print(f"Your {selection} is being dispensed. Enjoy!")
                lst['water'] -= 250
                lst['coffee'] -= 18
                lst['milk'] -= 150
                lst['money'] += 3.0
            else:
                print(f"Not enough money inserted. ${money_inserted} refunded!")



content={
'water':300,
'milk':200,
'coffee':76,
'money':0,
}
cont=True
while cont:
    choice=choose()
    if choice==2:
        cont=False
    elif choice==1:
        report(content['water'], content['coffee'],content['milk'],content['money'])
    elif check_ingredient(choice,content)==1:
        print(content)
        transaction(choice,handle_cash(),content)
        print(content)
    elif check_ingredient(choice,content)==0:
        error(choice,content)


