class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        answers = [0] * (W + 1)
        #W가 1일때 구한다