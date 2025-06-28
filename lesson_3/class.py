class Person:
    #Метод в классе = функция
    vid = 'homosapiens'
    
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def make_money(self):
        print(f'{self.name} в {self.age} лет заработал 1 млн рублей')

evg = Person(height = 176, age = 37, name = "Evgenii")

evg.make_money()