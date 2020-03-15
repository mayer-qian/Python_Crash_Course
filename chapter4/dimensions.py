#元组
dimensions = (200, 500)
print(dimensions[0])
print(dimensions[1])

#不能单独修改元素
#dimensions[0] =  199

print("==================================")
#但可以重新赋值

dimensions = (200, 500)
print("original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (300, 600)
print("\noriginal dimensions:")
for dimension in dimensions:
    print(dimension)