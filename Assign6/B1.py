#Using Generatorss

def fibonacciGenerator():
    first, second = 0, 1
    while True:
        yield first
        first, second = second, first + second

inputNum = int(input("Enter a number: "))
# generator = fibonacciGenerator()
# for i in range(inputNum):
#     print(next(generator), end=" ")


#Using Iterators
class FibonacciIterator:
    def __init__(self, n):
        self.n = n
        self.first, self.second = 0, 1
        self.length = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.length >= self.n:
            raise StopIteration
        
        resNum = self.first
        self.first, self.second = self.second, self.first + self.second
        self.length += 1
        return resNum

fibonacciSeries = FibonacciIterator(inputNum)
for i in fibonacciSeries:
    print(i, end=" ")
