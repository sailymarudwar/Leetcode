'''Given a 32-bit signed integer, reverse digits of an integer.
Example 1:
Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
Output: 21
'''


class Solution:
    def reverse(self, x):
        if x>=0:
            a = int(str(x)[::-1])
        if x < 0:
            a = -1 * (int((str(x)[1::])[::-1]))
        if a not in range(-2**31,2**31 - 1):
            return 0
        else:
            return a
sol = Solution()

sol.reverse(-321)

