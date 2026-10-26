# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:

    def findPosition(self, pairs: List[Pair], i: int) -> int:
        if i == 0:
            return 0
        key = pairs[i].key
        for j in range(i):
            candidateKey = pairs[j].key
            if candidateKey > key:
                return j
        return i

    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        out = []
        for i in range(len(pairs)):
            newPos = self.findPosition(pairs, i)
            if newPos == i:
                pass
            else:
                pair = pairs.pop(i)
                pairs.insert(newPos, pair)
            out.append(pairs.copy())
        return out