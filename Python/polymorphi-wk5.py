class Animal:
    def make_sound(self):
        print("Some generic animal sound")


# Dog class (inherits from Animal)
class Dog(Animal):
    def make_sound(self):
        print("Dog says: Woof! Woof!")


# Cat class (inherits from Animal)
class Cat(Animal):
    def make_sound(self):
        print("Cat says: Meow! Meow!")


# Creating objects
animal1 = Dog()
animal2 = Cat()

# Polymorphism in action!
animals = [animal1, animal2]

for animal in animals:
    animal.make_sound()
