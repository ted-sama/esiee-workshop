# In this python program we will work on classes and objects

# TASK 1: Let's create a class called Superhero
class Superhero:
    def __init__(self, name, gender, age, city):
        self.name = name
        self.gender = gender
        self.age = age
        self.city = city
        self.powers = []
        self.origin = None
        self.friends = []
    
    # TASK 2: Add Power, Origin and Friends attributes
    def set_power(self, power):
        self.powers.append(power)
        
    def remove_power(self, power):
        self.powers.remove(power)

    def set_origin(self, origin):
        self.origin = origin

    def add_friend(self, friend):
        self.friends.append(friend)
        
    def remove_friend(self, friend):
        self.friends.remove(friend)
        
    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Gender: {self.gender}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")
        print(f"Powers: {self.powers}")
        print(f"Origin: {self.origin}")
        print(f"Friends: {self.friends}")
        

# Justice League
batman = Superhero("Batman", "Male", 30, "Gotham City")
superman = Superhero("Superman", "Male", 30, "Metropolis")
wonder_woman = Superhero("Wonder Woman", "Female", 100, "Themyscira")
flash = Superhero("Flash", "Male", 27, "Central City")

# TASK 2
batman_powers = ["Intelligence", "Martial Arts", "Gadgets", "Millionaire"]
for power in batman_powers:
    batman.set_power(power)
batman.set_origin("Gotham City")
batman_friends = [superman.name, wonder_woman.name, flash.name, "Alfred", "Dick Grayson", "Barbara Gordon", "Damian Wayne", "Selina Kyle"]
for friend in batman_friends:
    batman.add_friend(friend)

superman_powers = ["Super Strength", "Super Speed", "Intelligence", "Flight", "Thermal Vision", "Super Hearing", "Super Smell", "Ice Breath"]
for power in superman_powers:
    superman.set_power(power)
superman.set_origin("Metropolis")
superman_friends = [batman.name, wonder_woman.name, flash.name, "Lois Lane", "Clark Kent", "Jimmy Olsen", "Perry White", "Krypto"]
for friend in superman_friends:
    superman.add_friend(friend)

print("----------------Batman Info----------------")
batman.print_info()
print("\n----------------Superman Info----------------")
superman.print_info()
