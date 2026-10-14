class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # 1. traverse the array using the front and back element
        left, right = 0, len(numbers) - 1
        
        while left < right:
        # 2. calcute the sum using the pointers
            summ = numbers[left] + numbers[right]

        # 3. compare if they add up to target
            
            if summ < target:
                left += 1
            elif summ > target:
                right -= 1
            else:
                return [left + 1, right + 1]

        # 4. return the index of the found elements


