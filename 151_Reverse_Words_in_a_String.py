'''Given an input string, reverse the string word by word.



Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.'''

class Solution:
    def reverseWords(self, s: str) -> str:
        #s = s.strip()
        #left, right = 0, len(s) - 1
        res = ""
        s1 = s.split(" ")
        for i in range(len(s1)-1,-1,-1):
            if (len(s1[i]) > 0):
                res = res+ s1[i].strip() +' '
        return res.strip()

s = Solution()

print(s.reverseWords("The sky is blue"))