print('\tЭкслюзивная компьютерная сеть')
print('\tТолько для зарегестрированных пользователей! \n')
securiti = 0
username = ''
while not username:
    username = input('Логин: ')
password = ''
while not password:
    password = input('Пароль: ')
if username == 'M.Dawson' and password == 'secret':
    print('Привет, Майк.')
    securiti = 5
elif username == "S.Meir" and password == 'civilization':
    print('Здравствуй Сид')
    securiti = 3
elif username == 'S.Miyamoto' and password == 'mariobros':
    print('Доброго времени суток. Сигеру')
    securiti = 3
elif username == 'W.Wright' and password == 'thesims':
    print('Как дела, Уилл?')
    securiti = 3
elif username == 'ILYARD' and password == 'IDilya':
    print('Приветствую, учащийся Илья!')
    securiti = 1
elif username == 'guest' and password == 'guest':
    print('Добро пожаловать к нам в гости.')
    securiti = 1
else:
    print('Войти в систему не удалось. Должно быть, вы не очень то и эксклюзивный гражданин\n')
if __name__ == "__main__":
    input("\n\nНажмите Enter чтобы выйти. ")
