#making the lists
available_pizzas = ['small pizza','medium pizza','large pizza']
available_toppings = ['pepperoni for small pizza','pepperoni for medium pizza','pepperoni for large pizza','extra cheese']
pizza_prices = {'small pizza': 15, 'medium pizza': 20, 'large pizza': 25}
topping_prices = {'pepperoni for small pizza': 2,'pepperoni for medium pizza': 3, 'pepperoni for large pizza': 3, 'extra cheese': 1}
sub_total = []
final_order = {}

#ordering a pizza
print("HI,WELCOME TO ORDER PIZZA")
order_pizza = True
while order_pizza:    
    print("PLEASE CHOOSE PIZZA: ")
    print()
    for pizzas in available_pizzas:
        print(pizzas)
        print()
    while True:
        pizza = input("WHICH PIZZA WOULD YOU LIKE TO ORDER?")
        if pizza in available_pizzas:
            print(f"YOU HAVE ORDERD A {pizza}.")
            sub_total.append(pizza_prices[pizza])
            break
        if pizza not in available_pizzas:
            print(f"I AM SORRY,CURRENTLY WE DON'T HAVE {pizza}.")

    #asking for extra toppings
    order_topping = True
    print("THIS IS THE LIST OF AVAILABLE EXTRA TOPPINGS: ")
    for toppings in available_toppings:
        print(toppings)
        print()
    while order_topping:
        extra_topping = input("WOULD YOU LIKE TO ADD EXTRA TOPPING? yes or no?")
        if extra_topping == "yes":
            topping = input("WHICH ONE WOULD YOU LIKE TO ADD?")
            if topping in available_toppings:
                final_order.setdefault(pizza, [])
                final_order[pizza].append(topping)
                print(f"WE HAVE ADDED {topping}.")
                sub_total.append(topping_prices[topping])
            else:
                print(f"I AM SORRY,WE DON'T HAVE {topping} AVAILABLE.")

        elif extra_topping == "no":
            break
    extra_pizza = input("WOULD YOU LIKE TO ORDER ANOTHER PIZZA?")
    if extra_pizza == "no":
        for key, value in final_order.items():
            print(f"\nYOU HAVE ODERED {key} PIZZA WITH {value}")
        check_order = True
        while check_order:
            print()
            order_correct = input("IS THIS CORRECT? yes/no ")
            if order_correct == "yes":
                check_order = False
                order_pizza = False
            if order_correct == "no":
                print(final_order)
                add_remove = input("WOULD YOU LIKE TO ADD OR REMOVE? ")
                if add_remove == "REMOVE":
                    remove = input("WHICH PIZZA WOULD YOU LIKE TO REMOVE? ")
                    del final_order[remove]
                    print(final_order)
                if add_remove == "ADD":
                    check_order = False

#finalizing the order
print(f"\nYOUR TOTAL ORDER PRICE IS: ${sum(sub_total)}")
print(f"\n...THANK YOU FOR ODERED PIZZA...")
