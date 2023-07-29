# Solution with HashSet
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)

        return False
    
    
# Solution with using Dictionary. Takes less time but more memory.    
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}

        for n in nums:
            if n in dic:
                return True
            else:
                dic[n] = 1

        return False   