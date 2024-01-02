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
#Second and right solution (0.43)
class Solution():
    def maxSumWithK(self,a, n, k):
    
        # To keep track of array element's left tail sum
        max_left_tail_sum = [0] * n
        max_left_tail_sum[0] = a[0]
        curr_sum = max_left_tail_sum[0]
        
        for i in range(1, n):
            curr_sum = max(a[i] + curr_sum, # There's a left tail of a[i] with positive element sum
                           a[i] # Don't take left tail of a[i] into consideration for k-element subarray expansion
                          )
            
            max_left_tail_sum[i] = curr_sum
        
        sum_k = sum(a[:k])
        ans = sum_k # Suppose sum of first k elements subarray is the solution
    
        for i in range(k, n):
            # Redifine sum_k: move current k-element array one position forward and calculate its elements sum
            sum_k += a[i] - a[i-k]
            # Choose current array in the loop between:
            ans = max(ans, # Current k element array element sum
                      sum_k, # One position forward current k element array element sum
                      sum_k + max_left_tail_sum[i-k] # Sum best left tail of sum_k (in terms of sum of its elements)
                     )
    
        return ans


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
