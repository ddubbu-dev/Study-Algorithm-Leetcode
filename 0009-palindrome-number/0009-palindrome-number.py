class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        arr = list(str(x))
        size = len(arr)
        for i in range(size):
            if arr[i] == arr[size-1-i]:
                continue
            return False

        return True
