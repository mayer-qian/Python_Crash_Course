#遍历key-value
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'femi'
}
for key, value in user_0.items():
    print("\nkey is " + key)
    print("value is " + value)


#遍历key

favorite_language = {
    'jen': "python",
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
friends = ['phil', 'sarah']
for name in favorite_language.keys():
# change to for name in favroite_language结果是一样的
    if name in friends:
        print("Hi, " + name.title() +
              ", I see your favorite language is " +
              favorite_language[name].title() +
              "!"
              )


print("========================================")
#按顺序遍历字典
for name in sorted(favorite_language.keys()):
    print(name.title() + ", thanks for you polling!")

print("========================================")
#遍历所有value
for language in favorite_language.values():
    print(language.title())

print("========================================")
#剔除重复的value
for language in set(favorite_language.values()):
    print(language.title())
