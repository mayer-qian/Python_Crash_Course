pizza = {
    'crust': 'thick',
    'toppings': ['mushroom', 'extra cheese'],
}

print("You ordered a " + pizza['crust'] + "-crust pizza" +
      "with the following topping:")
for topping in pizza['toppings']:
    print('\t' + topping)

print("============================================")

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'], 'phil': ['python', 'haskell'], }

for key, values in favorite_languages.items():
    print("\n" + key.title() + "'s favorite language are ")
    for value in values:
        print("\t" + value.title())
