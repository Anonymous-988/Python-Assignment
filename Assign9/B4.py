class SubsetGenerator:
    def __init__(self, numSet):
        self.subsetList = []
        self.numSet = numSet

    def generateSubsetList(self):
        self.subsetList = []
        self.getSubsets([], 0)
        return self.subsetList
    
    #Divide and Conquer Algorithm (Implemented backtracking)
    def getSubsets(self, currentSubset, index):
        self.subsetList.append(currentSubset[:])

        for i in range(index, len(self.numSet)):
            currentSubset.append(self.numSet[i])
            self.getSubsets(currentSubset, i + 1)
            currentSubset.pop()

if __name__ == "__main__":
    inputNumSet = [1,2, 3]

    obj1 = SubsetGenerator(inputNumSet)

    res = obj1.generateSubsetList()

    print(res)
