class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
      
        i = 0
        while True:
            tmp = ""
            for w in range(len(strs)):
                word = strs[w]
                if i > len(word)-1:
                    return common_prefix
                if w == 0: # 기준
                    tmp = word[i]
                elif tmp != word[i]:
                    return common_prefix
     
            common_prefix += tmp
            i += 1
