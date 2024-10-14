print("Добро пожаловать в ООО \"Системы безопасности\".")
print("--Безопасность наше второе имя\n")
password = input('Введите пароль: ')
if password == 'secret':
    print('Доступ открыт')
else:
    print("Доступ закрыт.")

if __name__ == "__main__":
    input("\n\nНажмите Enter чтобы выйти. ")