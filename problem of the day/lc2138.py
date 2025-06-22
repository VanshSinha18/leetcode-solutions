from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        # make resultant array
        res = []
        # iterate over the string 
        for i in range(0, len(s), k):
            # make chunks 
            chunk = s[i:i+k]
            # if the chunk is not of length k, fill the remaining with fill
            if len(chunk) < k:
                chunk += fill * (k - len(chunk))
            res.append(chunk)
        return res
    
# test cases
sol = Solution()
print(sol.divideString("abcdefghi", 3, "x"))
print(sol.divideString("abcdefghij", 3, "x"))
print(sol.divideString("abcdefghijk", 3, "x"))
print(sol.divideString("abcdefghijkl", 3, "x"))
print(sol.divideString("abcdefghijklm", 3, "x"))