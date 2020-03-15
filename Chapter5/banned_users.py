#检查特定值是否包含在列表中

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can spost a response if you wish")