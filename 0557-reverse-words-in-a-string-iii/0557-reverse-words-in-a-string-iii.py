class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
    #     stack=[]
    #     result=[]
    #     for ans in s:
    #         stack.append(ans)
    #     while(!stack.isEmpty())
    #         result=stack.pop()
    # return result
        word= s.split()
        reverse = [w[::-1] for w in word]
        return ' '.join(reverse)