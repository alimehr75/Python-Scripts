class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 != 0:
            return len(range(low, high+1, 2))
        else:
            return len(range(low, high, 2))

        # return len(list(filter(lambda x: x % 2 != 0, range(low, int((high**0.5))+1))))
