class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        number_str = str(x)
        str_len = len(number_str)
        for i in range(str_len//2):
            if number_str[i] != number_str[str_len-1-i]:
                return False

        return True