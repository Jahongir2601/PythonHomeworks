class Animal:
    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")

class Cow(Animal):
    def __init__(self, name, age, type, milk):
        super().__init__(name, age, type)
        self.milk = milk
    def produce_milk(self):
        print(f"{self.name} produces {self.milk} litres milk per week")

class Chicken(Animal):
    def __init__(self, name, age, type, egg):
        super().__init__(name, age, type)
        self.egg = egg
    def produce_egg(self):
        print(f"{self.name} produces {self.egg} eggs per week")

class Sheep(Animal):
    def __init__(self, name, age, type, wool):
        super().__init__(name, age, type)
        self.wool = wool
    def produce_wool(self):
        print(f"{self.name} produces {self.wool} kg wool per year")

if __name__ == "__main__":
    lorem = Cow(name="Lorem", age="3", type="walking", milk=5)
    ipsum = Chicken(name="Ipsum", age="4", type="walking", egg=10)
    dolor = Sheep(name="Lorem", age="2", type="walking", wool=2)
    
    print("Cow:")
    lorem.eat()
    lorem.sleep()
    lorem.produce_milk()

    print("\nChicken")
    ipsum.eat()
    ipsum.sleep()
    ipsum.produce_egg()

    print("\nSheep")
    dolor.eat()
    dolor.sleep()
    dolor.produce_wool()