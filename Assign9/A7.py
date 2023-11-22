class PairSumIndexFinder:
    def __init__(self, numberList) -> None:
        self.numberList = numberList

    def getIndexPair(self, TargetSum):
        num_dict = {}
        for index, num in enumerate(self.numberList):
            difference = TargetSum - num
            if difference in num_dict:
                return num_dict[difference], index
            num_dict[num] = index
        return None
    
if __name__ == "__main__":
    numberList = [10, 20, 10, 40, 50, 60, 70]
    targetSum = 50

    clasObj = PairSumIndexFinder(numberList)
    result = clasObj.getIndexPair(targetSum)

    if result:
        print(f"Sum of elements from {result[0]} and {result[1]} is {targetSum}")
    else:
        print(f"Sum of no 2 elements add up to {targetSum}")


