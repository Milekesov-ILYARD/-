import random
import string
def pass_gen(A = 12):
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
