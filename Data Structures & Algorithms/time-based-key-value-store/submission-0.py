class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:

        l, r = 0, len(self.timeMap[key]) - 1
        val = self.timeMap.get(key)
        res = ""

        while l <=r:
            m = (l + r) // 2

            if timestamp < val[m][0]:
                r = m - 1
            elif timestamp >= val[m][0]:
                res = val[m][1]
                l = m + 1
        return res


        
