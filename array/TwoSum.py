# easy non optimal solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        for i in range (0, size):
            for j in range(i+1, size):
                if nums[i] + nums[j] == target:
                    return i, j

# optimal solution using hash maps
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainderMap = {}
        for i, e in enumerate(nums):
            remainder = target - e
            if remainder in remainderMap:
                return remainderMap[remainder], i
            remainderMap[e] = i
