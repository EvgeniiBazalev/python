#Условия if/else/elif

age = int(input('Введите Ваш возраст: '))

if age > 65:
    print('Вы пенсионер')

elif 35 < age < 65:
    print('Вы наставник')

elif 18 < age < 35:
    print('Вы молодой специалист')

else:
    print('Вы молодой специалист')