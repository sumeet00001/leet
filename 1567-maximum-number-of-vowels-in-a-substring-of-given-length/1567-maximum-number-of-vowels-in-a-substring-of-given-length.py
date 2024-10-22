class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        sets = {'a','e','i','o','u'}
        curr=0
        for i in range(k):
            curr+=int(s[i] in sets)
        ans=curr

        for i in range(k,len(s)):
            curr+=int(s[i] in sets)
            curr-=int(s[i-k] in sets)
            ans=max(ans,curr)

        return ans    