#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        pack = []
        #W가 1일때 구한다
        for i in range(n+1):
            pack.append([])
            
            for w in range(W + 1):
                if i == 0 or w == 0: pack[i].append(0)
                elif wt[i-1] <= w:
                    pack[i].append(
                        max(
                            val[i - 1] + pack[i - 1][w - wt[i - 1]],
                            pack[i-1][w]
                        ))
                else: pack[i].append(pack[i - 1][w])
        return pack[-1][-1]
 