#User function Template for python3
#https://practice.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1/

class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,Items,n, ans=0):
        Items.sort(key=lambda x: x.value / x.weight, reverse=True)
        for i in Items:
            if W > i.weight: W, ans = W - i.weight, ans + i.value
            else: return ans + W * (i.value / i.weight)
        return ans
