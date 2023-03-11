name = input('Enter your name ')
while 1:
    if len(name) <3:
        print('name is too short')
        name = input('Enter your name ')
    elif len(name)>15:
        print('name is too long')
        name = input('Enter your name ')
    else:
        print('name is okay')
        break 