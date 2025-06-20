class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = x
        if(x<0):
            return False
        rex = 0
        while(x!=0):
            rex = rex*10+x%10
            x = x//10

        return rex == num

num = int(input())

solution = Solution()
print(solution.isPalindrome(num))