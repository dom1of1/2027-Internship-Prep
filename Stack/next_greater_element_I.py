#brute force
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # create a hashmap of numbers in nums1 to check against nums2 later
        # create a res array length of nums1 with each place initialized to -1
        # for each num in nums2: we check if its in nums1 first, if not we skip
        # if it is, we check the elements after it till we find the first greater element, then we set result's index to the value

        nums1_Map = {num:idx for idx, num in enumerate(nums1)}
        res = [-1] * len(nums1)


        for i in range(len(nums2)):
            curr = nums2[i]
            if curr not in nums1_Map:
                continue
            
            for j in range(i + 1, len(nums2)):
                if nums2[j] > curr:
                    idx = nums1_Map[curr]
                    res[idx] = nums2[j]
                    break
        
        return res

"""
Time Complexity - O(n * m)
where n = len(nums2) and m = len(nums1).
For each element in nums1, we may iterate through the remaining elements of nums2 until we find the next greater element or reach the end.

Space complexity - O(m) we create a Hashmap and results list the size of nums1
"""



# Optimal solution(monotonic stack)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # again we create a Hashmap of nums1 to check against nums2 later
        # we create our results list initialized to -1 for each position and our stack
        # We iterate through nums2 and continuously check if our stack is non-empty and if the curr element is greater than what is on top of our stack.
        # if the conditions pass, we pop the element on top of our stack. The curr element becomes its greater number.
        # we find its index for the results list from our hashmap and set the value to the curr element
        # finally, we append curr to the stack if it also belongs to nums1 so that we can search for its greater number.

        nums1_Map = {num:idx for idx, num in enumerate(nums1)}
        result = [-1] * len(nums1)

        stack = []

        for i in range(len(nums2)):
            curr = nums2[i]

            while stack and curr > stack[-1]:
                val = stack.pop()
                idx = nums1_Map[val]
                result[idx] = curr
            
            if curr in nums1_Map:
                stack.append(curr)
        
        return result

"""
Time Complexity - O(n)
We iterate through nums2 once. Each element is pushed onto the stack at
most once and popped from the stack at most once, so the total work is
O(n) (iteration) + O(n) (pushes) + O(n) (pops) = O(n).

Space Complexity - O(m)
We create a hashmap, a result list, and a stack, each of which can store
at most m elements.
"""