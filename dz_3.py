class Comp:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    def __str__(self):  
        return f"Процессор компьютера: {self.__cpu}, Память пкашки: {self.__memory}"        

    def get_cpu(self):
        return self.__cpu

    def get_memory(self):
        return self.__memory

    def set_cpu(self, cpu):
        self.__cpu = cpu
        print("Найтройка:", self.__cpu)

    def set_memory(self, memory):
        self.__memory = memory
        print("Найстройка:", self.__memory)

    def make_computations(self):
        return f"{self.__cpu}, {self.__memory}"

    def __eq__(self, other):
        return self.__cpu == other.__cpu and self.__memory == other.__memory
    
    def __ne__(self, other):
        return not self == other
    
    def __lt__(self, other):
        return self.__cpu < other.__cpu and self.__memory < other.__memory
    
    def __gt__(self, other):
        return self.__cpu > other.__cpu and self.__memory > other.__memory
    
    def __le__(self, other):
        return self.__cpu <= other.__cpu and self.__memory <= other.__memory
    
    def __ge__(self, other):
        return self.__cpu >= other.__cpu and self.__memory >= other.__memory

class Phone:
    def __init__(self, sim_cards_list):
        self.__smcards_lst = [sim_cards_list]
    
    def __str__(self):
        return f"Симки: {self.__smcards_lst[-1]}"

    def get_sim(self):
        return self.__smcards_lst

    def call(self, sim_card_number, call_to_number):
        if sim_card_number == 1:
            return f"Идет звонок на номер {call_to_number} с сим-карты-1 - Beeline"
        elif sim_card_number == 2:
            return f"Идет звонок на номер {call_to_number} с сим-карты-2 - O!"
        elif sim_card_number == 3:
            return f"Идет звонок на номер {call_to_number} с сим-карты-3 - Megacom"
        else:
            print("Ошибка")
    
class Smartphone(Comp, Phone):
    
    def __init__(self, cpu, memory):
        super().__init__(cpu, memory)

    def __str__(self):
        return super().__str__()

    def use_gps(self, location):
        print(f"Ищем маршрут до локации: {location}")

pc = Comp("AMD 5", "16 GB")
pc2 = Comp("Snapdagon", "32 GB")
print(pc)
print("Процессор пкшки:", pc.get_cpu())
print("Память пкшки:", pc.get_memory())
pc.set_cpu("AMD Ryzen-7")
pc.set_memory("32 GB")
print(pc.make_computations())

print(pc == pc2)
print(pc != pc2)
print(pc < pc2)
print(pc > pc2)
print(pc <= pc2)
print(pc >= pc2)


phone = Phone("Beeline, O!, Megacom")
print(phone)
phone.get_sim()
phone._Phone__smcards_lst
print(phone.call(1, '+9967065450535'))
print(phone.call(2, '+9967065450535'))
print(phone.call(3, '+9967065450535'))

smart = Smartphone("1 пар", "2 пар")
print(smart)
smart.use_gps("C.Ибраимова")