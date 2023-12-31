MENU = {
    "espresso": {
        "ingredientes": {
            "agua": 50,
            "cafe": 18,
        },
        "costo": 1.5,
    },
    "latte": {
        "ingredientes": {
            "agua": 200,
            "leche": 150,
            "cafe": 24,
        },
        "costo": 2.5,
    },
    "cappuccino": {
        "ingredientes": {
            "agua": 250,
            "leche": 100,
            "cafe": 24,
        },
        "costo": 3.0,
    }
}

profit = 0
resources = {
    "agua": 3000,
    "leche": 2000,
    "cafe": 1000,
}
def is_resouserce_sufficiente(order_ingredients):
    """"Retorna True cuando la orden se puede hacer y False cuando la orden no se puede hacer"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f'Lo siento no hay sufiente {item}')
            return False
    return True

def process_coins():
    """"Retorna el total de las monedas calculadas"""
    print("Por favor inserte las monedas. ")
    total = int(input("¿Cuantos cuartos de centavo?: ")) * 0.25
    total += int(input("¿Cuantos decimos de centavo?: ")) * 0.1
    total += int(input("¿Cuantas monedas de 5 centavos?: ")) * 0.05
    total += int(input("¿Cuantas monedas de a centavo?: ")) * 0.01
    return total

def is_transection_successful(money_recived, drink_cost):
    """"Retorna True cuando el pago es aceptado, o False cuando el dinero es insuficiente"""
    if money_recived >= drink_cost:
        change = round(money_recived - drink_cost, 2)
        print(f"Aqui esta {change} en cambio.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Lo siento fondos insuficientes")
        return False

def make_coffee(drink_name, order_ingredients):
    """"Deduce el requerimientos de los ingredientes"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Aqui esta tu Cafe {drink_name} que lo disfrutes")


is_on = True

while is_on:
    choice = input("¿Que le gustaria ordenar? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Agua: {resources['agua']}ml")
        print(f"Leche: {resources['leche']}ml")
        print(f"Café: {resources['cafe']}g")
        print(f"Dinero: ${profit}")
    else:
        drink=MENU[choice]
        if is_resouserce_sufficiente(drink['ingredientes']):
            payment = process_coins()
            if is_transection_successful(payment, drink['costo']):
                make_coffee(choice, drink['ingredientes'])

