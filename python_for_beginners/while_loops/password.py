user = input()
password = input()

# while True:
#     log_password = input()
#     if log_password == password:
#         print(f'Welcome {user}!')
#         break

#
# log_pass = input()
# while log_pass != password:
#     log_pass = input()
#
# print(f'Welcome {user}!')

wrong = False

for try_to_log_n in range(3):
    log_pass = input()
    if log_pass == password:
        print(f'Hello {user}')
        break
    if try_to_log_n == 2:
        wrong = True

if wrong:
    print('Login stopped')
