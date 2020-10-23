'''Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.'''


class Solution:
    def isValid(self, s):
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for brac in s:
            if brac in mapping:
                top_element = stack.pop() if stack else "#"
                if mapping[brac] != top_element:
                    return False
            else:
                stack.append(brac)
        return not stack


sol = Solution()

print(sol.isValid('(())()'))
