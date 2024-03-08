
class MyClass:
    """A simple example class"""
    i = 12345

    def helloworld(self):
        return 'hello world'


class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)


class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)


if __name__ == '__main__':
    x = MyClass()

    print(x.helloworld())

    dog = Dog("I am a pretty dog")
    dog.add_trick("test1")
    dog.add_trick("test2")
    print(dog.tricks)

    bag = Bag()
    bag.add("test1")
    bag.add("test2")
    bag.add("test3")
    print(bag.data)


