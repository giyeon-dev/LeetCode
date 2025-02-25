class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        
        ans = ""

        pointer1, pointer2 = 0, 0

        while pointer1 < len(word1) or pointer2 < len(word2):
            if pointer1 < len(word1):
                ans += word1[pointer1]
                pointer1 += 1
            
            if pointer2 < len(word2):
                ans += word2[pointer2]
                pointer2 += 1
       

        return ans