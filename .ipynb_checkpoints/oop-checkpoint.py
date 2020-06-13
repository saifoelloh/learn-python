class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print("Hello my name is ", self.name, "and my age is", self.age)

jhony = Person("Foo", 10)
jhony.name = "Jhony"
jhony.age = 30
jhony.greeting()

class Student(Person):
    def __init__(self, name, age, room):
        super().__init__(name, age)
        self.room = room

    def say_hello(self):
        print("Hello my name is ", self.name, ", I'am", self.age, "yo and my room is", self.room)


peter = Student("Poter", 20, "Fo bar")
peter.name = "Peter"
peter.age = 23
peter.room = "Azkaban"
peter.greeting()
peter.say_hello()
