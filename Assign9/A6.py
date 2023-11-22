class ThreeSum:
    def __init__(self, nums = []) -> None:
        self.nums = nums

    def zeroSumElements(self):
        self.nums.sort()
        result = []

        for i in range(len(self.nums) - 2):
            if i > 0 and self.nums[i] == self.nums[i - 1]:
                continue
            left, right = i + 1, len(self.nums) - 1

            while left < right:
                total = self.nums[i] + self.nums[left] + self.nums[right]
                if total == 0:
                    result.append([self.nums[i], self.nums[left], self.nums[right]])
                    while left < right and self.nums[left] == self.nums[left + 1]:
                        left += 1
                    while left < right and self.nums[right] == self.nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result

# Input array
inputList = [-25, -10, -7, -3, 2, 4, 8, 10]

# Create an instance of the ThreeSum class
numsObj = ThreeSum(inputList)

# Find and print three elements with sum zero
result = numsObj.zeroSumElements()
print(result)
