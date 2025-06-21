dic_name_age = {'John': 32, 'Ella': 22, 'Cat': 9}

# for i in dic_name_age:
#     print(i)

total_workers = 0
total_age = 0

for (i, j) in dic_name_age.items(): #items возвращает кортеж ключ значение
    total_age += j
    total_workers += 1

print(total_age/total_workers)