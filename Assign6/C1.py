class French:
    def greet(self):
        print("Bonjour!!")

class Hindi:
    def greet(self):
        print("Namaskar!!")

class Italian:
    def greet(self):
        print("Ciao!!")

class Spanish:
    def greet(self):
        print("Hola!!")

class Japanese:
    def greet(self):
        print("Kon'nichiwa!!")
 

frenchObj = French()
hindiObj = Hindi()
italianObj = Italian()
spanishObj = Spanish()
japaneseObj = Japanese()

objList = [frenchObj, hindiObj, italianObj, spanishObj, japaneseObj]


# Demonstrate duck typing with the `greet` function
for obj in objList:
    obj.greet()