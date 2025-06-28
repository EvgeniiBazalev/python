def check_temp(temp):
    if temp > 36.75:
        return 'Похоже вы заболели'
    elif  temp < 36.2:
        return 'Аномально низкая температура'
    return 'Все ок' 


#human_temp = float(input('Введите температуру: '))

#print(check_temp(human_temp))

shop_list = ['Крем', "Деньги", "Шляпа", "Чумадан"]

def check_list(list):
    buy = 'Я купил:'
    for i in list:
        if i == list[len(list) - 1]:
            buy = buy + ' ' + i + '.'
        else:
            buy = buy + ' ' + i + ','
    print(buy)
    return buy

check_list(shop_list)