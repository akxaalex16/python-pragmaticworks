# Object-Oriented Programming
# modeling real world things or concepts
# technique to tackle complexity
# OOP:
# classes
# data abstraction
# encapsulation
# information hiding
# inheritance
# polymorphism

# class is a way to package properties and functions that are related
# initiated with the class command
# setup with __init__()  ---> which is called a constructor

class Car:
    def __init__(self,make, model):
        self.make = make
        self.model = model

        self.fuel_tank_size = 12
        self.current_fuel = 5

    def fill_tank(self):
        self.current_fuel = self.fuel_tank_size


my_honda = Car("Honda", "Accord")
my_honda.fill_tank()
print(my_honda.current_fuel)

# each time a class is called a new "Instance" is created
meep_meeps_bmw = Car("BMW", "6x")
print(meep_meeps_bmw.make)


class ElectricCar(Car):
    def __init__(self, make, model):

        super().__init__(make, model)
        self.battery_size = 100
        self.current_charge = 75

    def fill_tank(self):
        print("This car has no gas tank")

    def charge(self):
        self.current_charge = self.battery_size


my_tesla = ElectricCar("Tesla", "X")
my_tesla.charge()
print(my_tesla.current_charge)

# Car is the parent class and ElectricCar can inherit functions/methods from that parent class


# practical
class User:
    def __init__(self, first_name, last_name,
                 avatar_url, username, profile_info):
        self.first_name = first_name
        self.last_name = last_name
        self.avatar_url = avatar_url
        self. username = username
        self.profile_info = profile_info
        self.access = ["Can view profiles", "Update own profile"]

    def get_user_information(self):
        print(f'Username: {self.username}')
        print(f'Name: {self.first_name} {self.last_name}')
        print(f'Information: {self.avatar_url} \n {self.profile_info}')

    def check_access(self, access):
        return self.access.count(access) > 0


new_user = User("Akse", "Dee", "www.avatars.com/Akse",
                "AkSeDee123", "Princess of Genovia")
print(new_user.profile_info)
print(new_user.get_user_information())
print(new_user.check_access("Can view profiles"))
# returns true


class Admin(User):
    def __init__(self,  first_name, last_name,
                 avatar_url, username, profile_info):
        super().__init__(first_name, last_name,
                         avatar_url, username, profile_info)
        self.access = ["Can edit Users"]


new_admin = Admin("Xaan", "Alhu", "www.avatars.com/Xaanalhu", "XaanAlhu123", "Prince of Genovia")
print(new_admin.access)

