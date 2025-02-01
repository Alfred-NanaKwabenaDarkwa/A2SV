class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = strs[0]
        for i in strs:
            t = ""
            if len(lcp) < len(i):
                l_i = len(lcp)
            else:
                l_i = len(i)
            t = ''
            for j in range(l_i):
                if lcp[j] == i[j]:
                    t += lcp[j]
                else:
                    break
        lcp = t
        return lcp