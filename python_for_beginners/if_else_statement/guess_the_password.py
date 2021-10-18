PASSWORD_TEMPLATE = "s3cr3t!P@ssw0rd"
WELCOME_MESSAGE = "Welcome"
WRONG_MESSAGE = "Wrong password!"

password = str(input('Your password'))

if password == PASSWORD_TEMPLATE:
    print(WELCOME_MESSAGE)
else:
    print(WRONG_MESSAGE)
