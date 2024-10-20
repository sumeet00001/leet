class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        lists=list(s)
        i=0
        j=len(s)-1
        while i < j:
            if not lists[i].isalpha():
                i+=1
            elif not lists[j].isalpha():
                j-=1
            else:
                lists[i],lists[j]=lists[j],lists[i]
                i+=1
                j-=1
        return ''.join(lists)
           