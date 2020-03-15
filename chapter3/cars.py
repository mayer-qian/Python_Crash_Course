#排序(正序)，按照字母，永久修改，无法恢复

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

#倒序,按照字母

cars.sort(reverse=True)
print(cars)

print("=======================================")

#sorted不会改变原始数据
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print(sorted(cars))
print(cars)

print("=======================================")

#反向
print(sorted(cars, reverse=True))
print(cars)


print("=======================================")

#list里的反向
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

print("=======================================")

#确定列表的长度
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

