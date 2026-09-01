class TimeMap:
    # create a hashmap { key :[[value, time]] }
    # for the get, we can perform a binary search on the list for a key.
    # if the value of the pair at the mid index is our target, return that value.
    # If it is less than our target, we continue searching to the right for a potentially closer value.
    # else if it is greater, we search on the left.

    def __init__(self):
        self.store = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        
        self.store[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        times = self.store.get(key, [])

        #binary search
        l, r = 0, len(times) - 1

        while l <= r:
            mid = (l + r) // 2

            if times[mid][1] == timestamp:
                return times[mid][0]
            
            elif times[mid][1] < timestamp:
                # Valid candidate; look for a closer timestamp
                result = times[mid][0] 
                l = mid + 1
            
            else:
                r = mid - 1
        
        return result

'''Time Complexity 
Set method - O(1)
Get method - O(log(n)) where n is the size of the key's list

Space Complexity - O(n) where n is the number of set operations (number of [value,timestamp] pairs stored)
'''