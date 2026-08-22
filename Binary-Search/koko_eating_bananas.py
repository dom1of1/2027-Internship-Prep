class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        #function to check if k value allows us to finish piles
        def check_piles(k):
            curr_h = 0
            for num in piles:
                curr_h += -(num//-k) #getting the ceiling value 
                if curr_h > h:
                    return False
            
            return True
 
        # binary search on possible k values
        l, r = 1, max(piles)

        while l <= r:
            mid = (l + r) // 2

            if check_piles(mid):
                r = mid - 1
            
            else:
                l = mid + 1
        
        return l # the left pointer is the min_k. 

# Time Complexity - O(n * log(max(piles)))
# Space Complexity - O(1)     



     
        

        
                

