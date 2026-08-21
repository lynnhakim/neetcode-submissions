class TimeMap:

    def __init__(self):
        self.table = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.table: 
            self.table[key].append((timestamp, value))
        else:
            self.table[key] = [(timestamp, value)]


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.table:
            return ""
        
        lo, hi = 0, len(self.table[key])
        while lo < hi: 
            mid = (lo + hi)//2
            if self.table[key][mid][0] == timestamp: 
                return self.table[key][mid][1]
            elif self.table[key][mid][0] > timestamp: 
                hi = mid 
            else:
                lo = mid + 1
        print(lo)
        return self.table[key][lo - 1][1] if lo > 0 else ""

