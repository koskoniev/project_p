class Car_owner:
    def __init__(self, name, about=None):
        self.name = name
        self.about = about
    def __str__(self):
        return f"{self.name}"

class Car:
    def __init__(self, i_model, i_year, i_descr):
        self.model = i_model
        self.year = i_year
        self.descr = i_descr
    def __str__(self):
        return f"{self.model} {self.year} {self.descr}"

class Garage:
    def __init__(self, user):
        self.user = user
        self.storage = dict()
    def add_item(self, item, cnt):
        self.storage[item] = cnt
    def get_item(self):
        return self.storage
    def __str__(self):
        tmp = str()
        for item, count in self.storage.items():
            tmp += f"{str(item)}: {count}\n"
        return f"Garage: {self.user}\nItems:\n{tmp}" 



# kungfury = Car_owner("Kung Fury")
# kungfury.about = "Do my job"
# terminator = Car_owner("T1000", "liquid")
# # print(kungfury.name, kungfury.about)
# # print(terminator.name, terminator.about)

# models = ['bmw', 'mers', 'toyota', 'lada']
# descriptions = ['sedan', 'red', 'diesel', 'zapchasti']
# car1 = Car('bmw', 2000, 'sedan')
# car2 = Car('mers', 2005, 'red')
# car3 = Car('toyota', 1990, 'diesel')
# car4 = Car('lada', 1995, 'zapchasti')
# # print(car1.model, car1.year, car1.descr)
# # print(car2.model, car2.year, car2.descr)
# # print(car3.model, car3.year, car3.descr)
# # print(car4)

# g1 = Garage(kungfury)
# g2 = Garage(terminator)
# g1.add_item(car1, 1)
# # print(g1)
# g1.add_item(car2, 2)
# print(g1)
# # print(g2.user.name, g2.storage)
# # print(g1.user.name, g1.get_item())

