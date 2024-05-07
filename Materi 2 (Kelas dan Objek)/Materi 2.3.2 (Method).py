class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print("Hello, my name is", self.name, "and I am", self.age, "years old.")

person1 = Person("John", 25)
person1.greeting() # Output: Hello, my name is John and I am 25 years old.
