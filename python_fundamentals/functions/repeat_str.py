def repeat_string(string, rep):
    result = ''
    for i in range(rep):
        result += string
    return result

string = input()
rep = int(input())

print(repeat_string(string, rep))




