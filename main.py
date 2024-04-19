# from random import 
import uuid

class Man:
    def __init__(self, name):
        self.name = name
        self.id = str(uuid.uuid4())[:8]

class Pers(Man):
    def __init__(self, name, unit="", level=0):
        super().__init__(name)
        self.unit = unit
        self.level = level
    def get_level(self):
        return self.level
    def level_up(self):
        self.level += 1
    def level_down(self):
        self.level -= 1
    def __str__(self):
        return f"{self.name} {self.unit}"

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()
    def add_gr(self, pers):
        self.group.add(pers)
    def get_gr(self):
        t = ""
        for i in self.group:
            t += f"{i.id} {i.name} {i.level} {i.unit}\n"
        return f"{self.number}: \n{t}"
    def delete_gr(self, name):
        # t = tuple(self.group)
        # for i in t:
        for i in tuple(self.group):
            if i.name == name:
                self.group.remove(i)

        # return self.group
    def find_pers(self, name):
        for i in self.group:
            if i.name == name:
                print(i.name, i.id)
        


a = Pers("a")
a.unit = "Astronaut"
b = Pers("b")
b.unit = "Badboy"
c = Pers("c")
c.unit = "Caesar"
d = Pers("d")
# print(a)
g = Group("G_")
g.add_gr(a)
g.add_gr(b)
g.add_gr(c)
g.add_gr(d)
print(g.get_gr())
# g.find_pers("a")
g.delete_gr('a')
print(g.get_gr())
