alien_0 = {'color': 'green', 'point': 5}
print(alien_0['color'])
print(alien_0['point'])

#添加key-value

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#赋值

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("original x_position is " + str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("new x_position is " + str(alien_0['x_position']))


print("删除key-value")
alien_0 = {'color': "green", 'points':5}
del alien_0['color']
print(alien_0)


print("============================")

#较长的字典推荐的格式

favorite_language = {
    'jen': "python",
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

print("Sarah's favorite language is " +
      favorite_language['sarah'].title() +
      ".")
