class Solution:
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        maxlen = 0

        for sublen in range(0,len(s)+1):
            sublen = len(s) - sublen
            start = 0
            end = sublen
            while(end <= len(s)):
                sub = s[start:end]
                max_c = 0
                for char in sub:
                    if sub.count(char) > max_c:
                         max_c = sub.count(char)
                if (sublen - max_c) <= k:
                    maxlen = max([maxlen, sublen])
                start += 1
                end += 1
            if maxlen > sublen:
                break
            
        return maxlen
        


if __name__ == "__main__":
    a = Solution()
    b = a.characterReplacement("ABAB", 2)
    print(b)
        
