# Циклы for и range и while

import time

fruit = ['яблоки', "клубника", "черешня", "дыня", "арбузы"]

for i in fruit:
    print(f'У нас новое поступление: {i}')
    time.sleep(1.6)
    print(time.localtime())