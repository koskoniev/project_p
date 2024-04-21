from man import *

man = Pers("Dude")
print(man)
man.add_info("id", "1234567890")
man.add_info("phone", "+0987654321")
man.add_info("email", "dude@example.com")

# car = Car("honda", 0000, "civic")
# print(car)

# print(man.get_info("id", 'email', 'phone'))
# print(man.get_info("id"))
print(man.get_info())
print(man.get_info("id"))
t = ("phone", "email")
# print(type)
print(man.get_info("phone", "email"))
print(man)

# d1 = dict(id="1234567890", phone="+0987654321", email="dude@example.com")
# print(d1)
# t = ("id", "email")
# # print(t)

# print(t)

# print(d1.keys())
# # dt = dict(lambda dt: {dt[x]: d1[x]} for x in t)



# list_dict = [
#     {'a': 1, 'b': 2},
#     {'a': 3, 'b': 4}]

# result = list(map(lambda x : x.get('a'), list_dict))

# print(result)
