'''Count the number of prime numbers less than a non-negative number, n.



Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0


Constraints:

0 <= n <= 5 * 106'''


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # My own way
        if n <= 2:
            return 0

        isPrime = [True] * n
        for i in range(2, n):
            if isPrime[i]:  # Number of index i is a prime number
                j = 2  # Times start from 2
                while i * j < n:
                    isPrime[i * j] = False
                    j += 1
            else:
                continue

        cnt = 0
        for i in range(2, n):
            if isPrime[i]:
                cnt += 1

        return cnt

