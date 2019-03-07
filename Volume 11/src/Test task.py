# task #2002
# Difficulty 67
login = []
commands = []
pwd = {}
loggedIn = {}
j = int(input())
for m in range(j):
    commands.append(input().split('\n'))
for i in range(len(commands)):
    cmd = commands[i][0].split()
    if cmd[0] == 'register':
        if cmd[1] in login:
            print('fail: user already exists')
        else:
            login.append(cmd[1])
            pwd[cmd[1]] = cmd[2]
            loggedIn[cmd[1]] = 'No'
            print('success: new user added')
    elif cmd[0] == 'login':
        if cmd[1] not in login:
            print('fail: no such user')
        elif cmd[2] != pwd[cmd[1]]:
            print('fail: incorrect password')
        elif loggedIn[cmd[1]] == 'Yes' or None:
            print('fail: already logged in')
        else:
            loggedIn[cmd[1]] = 'Yes'
            print('success: user logged in')
    elif cmd[0] == 'logout':
        if cmd[1] not in login:
            print('fail: no such user')
        elif loggedIn[cmd[1]] == 'No':
            print('fail: already logged out')
        else:
            loggedIn[cmd[1]] = 'No'
            print('success: user logged out')

