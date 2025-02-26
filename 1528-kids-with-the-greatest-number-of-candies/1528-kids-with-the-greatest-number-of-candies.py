class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []

        for candy in candies:
            if candy + extraCandies >= max(candies):
                ans.append(True)
            else:
                ans.append(False)

        return ans


        
        