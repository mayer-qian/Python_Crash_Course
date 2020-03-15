cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print("=======================")

#使用！=代表不等于
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")