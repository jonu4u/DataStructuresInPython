class Solution:
    def __init__(self,size=10000):
        self.ans=""
        # Max length given in constrainsts
        self.memoizize_top_down=[]

    # Recursion
    def LCS_RC(self, s1, s2, size1, size2, common):
        # Base Case
        if size1==0 or size2==0:
            return common
        # Choice Diagram
        c2=common
        if s1[size1-1]==s2[size2-1]:
            c2= self.LCS_RC(s1, s2, size1 - 1, size2 - 1, common + s1[size1 - 1])
        left=self.LCS_RC(s1, s2, size1 - 1, size2, "")
        right=self.LCS_RC(s1, s2, size1, size2 - 1, "")
        max_string=max([c2,left,right],key=len)
        return max_string

    def LCS_top_down(self, s1, s2, size1, size2):
        # Base Case
        self.memoizize_top_down=[["" for i in range(0, size1 + 1)] for i in range(0, size2 + 1)]
        self.ans=""
        for row in range(0,size1+1):
            for col in range(0,size2+1):
                if row==0 or col==0:
                    self.memoizize_top_down[row][col]= ""

                # Choice Diagram
                elif s1[row-1]==s2[col-1]:
                    self.memoizize_top_down[row][col]= self.memoizize_top_down[row - 1][col - 1] + s1[row - 1]
                    self.ans=max([self.memoizize_top_down[row][col], self.ans], key=len)
                else:
                    self.memoizize_top_down[row][col]= ""
        return self.ans




s=Solution()
print(s.LCS_top_down("bacabab", "babacab", 7, 7))
print(s.LCS_top_down("aacabdkacaa", "aacakdbacaa", 11, 11))
