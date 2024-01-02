"""
Given an array a of length n and a number k, find the largest sum of the subarray
containing at least k numbers. It is guaranteed that the size of array is at-least k.
#########################################################################
Example 1:

Input : 
n = 4
a[] = {-4, -2, 1, -3}
k = 2
Output : 
-1
Explanation :
The sub-array of length at-least 2
that produces greatest sum is {-2, 1}
#########################################################################
Example 2:
Input :
n = 6 
a[] = {1, 1, 1, 1, 1, 1}
k = 2
Output : 
6
Explanation :
The sub-array of length at-least 2
that produces greatest sum is {1, 1, 1, 1, 1, 1}
#########################################################################

Your Task:  
You don't need to read input or print anything. Your task is to complete the
function maxSumWithK() which takes the array a[], its size n and an integer k
as inputs and returns the value of the largest sum of the subarray containing
at least k numbers.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Constraints:
1 <= n <= 105
-105 <= a[i] <= 105
1 <= k <= n
"""

# Wrong solution because take largest sum among elements of the array
# instead of subarray with largest sum.
class Solution():
    def maxSumWithK(self, a, n, k):
        l = sorted(a)
        l = l[::-1]
        l_k = l[:k]
        l_check = l[k:]
        for i in l_check:
            if i>=0:
                l_k.append(i)
            else:
                break
        return sum(l_k)