#使用函数range生成数字，从1开始到5结束，不包含5

for value in range(1, 5):
    print(value)

print("=======================================")

#用range创建数字列表

numbers = list(range(1, 6))
print(numbers)

print("=======================================")
#定义步长

even_numbers =  list(range(2, 11, 2))
print(even_numbers)
print("=======================================")

#将1-10的平方添加到列表

squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

print("=======================================")

#列表解析
squares = [value**2 for value in range(1, 11)]
print(squares)
print("=======================================")

#求大，求小，求和
digits = list(range(1, 11))
print("max digit is " + str(max(digits)))
print("min digit is " + str(min(digits)))
print("sum of digit is " + str(sum(digits)))

print(sum(list(range(1, 1000000))))

#打印3到30内3的倍数
digis = list(range(3, 31, 3))
for digi in digis:
    print(digi)

#1-10的立方
lifang = [value**3 for value in range(1, 11)]
print(lifang)

