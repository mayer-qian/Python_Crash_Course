# 变量值不会变
favorite_language = ' python '
print(favorite_language.lstrip())
print(favorite_language)

# 变量值通过赋值可以改变
favorite_language = ' python '
favorite_language = favorite_language.lstrip()
print(favorite_language)

# 剔除左边空白，剔除空白，同时剔除左右。
favorite_language = ' python '
print(favorite_language.lstrip())
print(favorite_language.rstrip())
print(favorite_language.strip())
