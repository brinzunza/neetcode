"""
input: str key, str value, int timestamp
output: str value of timestamp <= input timestamp
"""

class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store.keys():
            self.store[key].append([value, timestamp])
        else:
            self.store[key] = [[value, timestamp]]
        return 

    def get(self, key: str, timestamp: int) -> str:
        if(key not in self.store.keys()):
            return ""
        wantedKey = self.store[key]
        start = 0
        end = len(wantedKey) - 1

        if wantedKey[start][1] > timestamp:
            return ""

        mid = (start + end) // 2
        while start < end:
            if wantedKey[mid][1] == timestamp:
                return wantedKey[mid][0]
            if end - start == 1:
                if wantedKey[end][1] <= timestamp:
                    return wantedKey[end][0]
                else:
                    return wantedKey[start][0]
            elif timestamp > wantedKey[mid][1]:
                start = mid
            else:
                end = mid
            mid = (start + end) // 2
        return wantedKey[start][0]

"""
Time complexity: init = O(1), set = O(1), get = O(logn)
space complexity: init = O(n), set = O(1), get = O(1)
"""