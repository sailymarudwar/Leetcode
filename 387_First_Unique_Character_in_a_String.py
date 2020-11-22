'''Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.


Note: You may assume the string contains only lowercase English letters.'''
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = defaultdict(int)
        for c in s:
            d[c] +=1
        for idx, ch in enumerate(s):
            if d[ch] == 1:
                return idx
        return -1

    def approach2(self, s: str) -> int:
        count = collections.Counter(s)

        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1