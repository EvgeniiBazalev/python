#Словари - они изменяемые
#Словари имеют ключ и значение


dic_name_age = {'John': 32, 'Ella': 22, 'Cat': 9}
v = dic_name_age.get("John")
dic_name_age['Doggy'] = 99
val_Dog = dic_name_age.pop("Doggy")
dic_name_age['Ella'] = val_Dog
print(val_Dog)
print(dic_name_age)