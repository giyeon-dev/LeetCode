class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        pointer = 0
        len1, len2 = len(word1), len(word2)
        ans = ""

        while pointer < len1 and pointer < len2:
            ans += word1[pointer]
            ans += word2[pointer]
            pointer += 1

        if pointer < len1:
            ans += word1[pointer:]

        if pointer < len2:
            ans += word2[pointer:]
            
        return ans
        
