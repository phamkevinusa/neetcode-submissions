class TimeMap:

    def __init__(self):
        self.keyStore = {} #map of key:[[value,timestamp]]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = [] #initialize list in dict for key

        self.keyStore[key].append([value,timestamp]) # add values to list for key

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.keyStore.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l+r) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res
