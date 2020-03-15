alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

print('=====================================')
#创建30个外星人
aliens = []
for number in range(30):
    alien = {'color': 'green', 'points': 5}
    aliens.append(alien)

for alien in aliens[0:5]:
    print(alien)
print(".....")


print('=====================================')
#批量修改属性

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
for alien in aliens[0:5]:
    print(alien)