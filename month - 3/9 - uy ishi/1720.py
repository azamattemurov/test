class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        out = [first]
        n = len(encoded)

        for i in range(n):
            out.append(out[i] ^ encoded[i])

        return out