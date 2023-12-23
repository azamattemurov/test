class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        occ ={}
        for i, c in enumerate(s):
            if c in occ:
                if i - occ[c]-1 != distance[ord(c)-ord('a')]:
                    return False
            else:
                occ[c] = i
        return True