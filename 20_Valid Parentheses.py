'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.'''


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapp = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in mapp:
                top_element = stack.pop() if stack else "#"
                if mapp[c] != top_element:
                    return False
            else:
                stack.append(c)
        return not stack

s = Solution()
print(s.isValid('(())['))