#修改列表

motocycles = ['honda', 'yamaha', 'suzuki']

motocycles[0] = 'ducati'
print(motocycles)

#列表末添加元素

motocycles = ['honda', 'yamaha', 'suzuki']
motocycles.append('ducati')
print(motocycles)

#add data to empty list

ultramans = []
ultramans.append('ace')
ultramans.append('jack')
ultramans.append('Taro')
print(ultramans)

#add data to specific location

ultramans.insert(0, 'zoffy')
print(ultramans)

#delete data by del

del ultramans[0]
print(ultramans)

#delelte data by pop, default is last

print(motocycles)
poped_motocycle = motocycles.pop()
print(motocycles)
print(poped_motocycle)

# delete specific data by pop

print(motocycles)
motocycles.pop(1)
print(motocycles)

#pop 可以有返回值，del没有，根据实际情况选择。

#根据值删除,remove和del一样没有返回值，但是由于需要定义具体删除的值，所以可以赋值到变量

motocycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motocycles)
motocycles.remove('suzuki')
print(motocycles)


motocycle = 'yamaha'
print("deleted brand is " + motocycle)
motocycles.remove(motocycle)
print(motocycles)

