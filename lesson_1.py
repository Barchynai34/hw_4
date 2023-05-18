#class - Чертеж
#__init__ - Конструктор
# self - Сам обьект \ адрес на обьект
#self.model - Аиирибут обьекта
# model, color, year - Входящие параметры
#def drive(self): - Методы


class Car:
    wheel = 4

    def __init__(self, model, color, year, penalties=[]):
        self.model = model
        self.color = color
        self.year = year 
        self.penalties = penalties

    def drive(self, city):
        print(f"Машина {self.model} едет в {city}")
    
    def info(self):
        print(f"{self.model} {self.color} {self.year} {self.penalties}")

    def change_color(self, new_color):
        self.color = new_color


        




mers = Car("Mersedes Benz", "Black", 2023, [30000])
mers.info()

# mers.color = "White" #меняем атрибут обьекта
# mers.info()

# mers.change_color(new_color="Blue")
# mers.info()

# print(f"{mers.model} {mers.color} {mers.year}")
# mers.drive("Ош")

bmw = Car(color="Red",model="BMW M5",  year=2022, penalties=[10, 39, 40])
bmw.info()
# bmw.drive("Бишкек")

# Car.wheel = 8
# bmw.wheel = 6
# print(bmw.wheel)
# print(Car.wheel)