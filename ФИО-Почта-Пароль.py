
import random
import string
def email_gen(list_of_names):
    emails = []
    for i in list_of_names:
        letter = 1
        while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
            letter+=1
        emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
    return emails

def pass_gen(A=9):  # генерация пароля
    symbols = '!@#$%^&*()-+'
    password = ''
    var = [string.digits, string.ascii_uppercase, string.ascii_lowercase, symbols]
    password += random.choice(string.digits)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.ascii_lowercase)
    password += random.choice(symbols)
    while len(password) < A:
        password+=random.choice(var[random.randint(0,3)])
    return password



with open("input.txt") as file1:
    l = file1.readline()
    lis = []
    strings = []
    for line in file1:  #
        s = line.split(',')
        lis.append([s[1].strip(), s[2].strip()])
        strings.append([s[1].strip(), s[2].strip(), s[3].strip(), s[4]])
    emails = email_gen(lis)

with open("output.txt", 'w') as file2:
    file2.write(l)
    n = 0
    for i in range(len(strings)):
        file2.write(emails[n]+', '+pass_gen(12)+', '+strings[i][0]+', '+strings[i][1]+', '+strings[i][2]+', '+strings[i][3])
        n += 1







