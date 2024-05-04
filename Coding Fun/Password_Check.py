# Simple Password Checker

# Get Original Password
passwordFile = open('SecretPasswordFile.txt')
secretPassword = passwordFile.read()

# Get User Input
typedPassword = input('Enter your password: ')

# Conditions
if typedPassword == secretPassword:
    print('Access Granted')
    if typedPassword == '12345':
        print('That password is the one that an idiot puts on their luggage.')
else:
    print('Access Denied')
