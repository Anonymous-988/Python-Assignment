class Animal:
    def __init__(self):
        pass

    def reply(self):
        self.speak()

class Mammal(Animal):
    def __init__(self):
        super().__init__()
    
class Cat(Mammal):
    def __init__(self):
        super().__init__()

    def speak(self):
        print("Meow!!!")

class Dog(Mammal):
    def __init__(self):
        super().__init__()

    def speak(self):
        print("Bhow bhow!!!")

class Primate(Mammal):
    def __init__(self):
        super().__init__()

class Hacker(Primate):
    def __init__(self):
        super().__init__()

    def speak(self):
        print("Hackurr!!!")

if __name__ == "__main__":
    HackerObj = Hacker()
    print("Hacker Says: ",end="")
    HackerObj.reply()

    CatObj = Cat()
    print("Cat Says: ",end="")
    CatObj.reply()

    DogObj = Dog()
    print("Dog Says: ",end="")
    DogObj.reply()
