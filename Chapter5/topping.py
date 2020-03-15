requested_toppings =  ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now")
    else:
        print("adding " + requested_topping)
print("\nfinished making your pizza")

print("===========================================")
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping)
    else:
        print("Sorry,we don't have " + requested_topping)
print("\nfinished making your pizza")