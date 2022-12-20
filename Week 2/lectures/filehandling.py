username_pwd = open('passwords.txt','r').read()
username_pwd = username_pwd.split()

for uname_pwd in username_pwd:
    username, password = uname_pwd.split(',')
    print(f"the password of username {username} is {password}")