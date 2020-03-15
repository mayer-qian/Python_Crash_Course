players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:3])
#从第三个数字到最后
print(players[2:])
#最后三个
print(players[-3:])
print(players[-3:-2])
print(players[-3:-1])
print(players[-3:0])
print(players[-3:1])

print("=======================================")

print("Here are the first three players on my team: ")
for player in players[0:3]:
    print(player.title())