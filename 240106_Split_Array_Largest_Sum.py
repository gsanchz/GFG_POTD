"""
Given an array arr[] of N elements and a number K., split the given array into K
subarrays such that the maximum subarray sum achievable out of K subarrays formed
is minimum possible. Find that possible subarray sum.

########################################################################################
Example 1:

Input:
N = 4, K = 3
arr[] = {1, 2, 3, 4}
Output: 4
Explanation:
Optimal Split is {1, 2}, {3}, {4}.
Maximum sum of all subarrays is 4,
which is minimum possible for 3 splits.
########################################################################################
Example 2:

Input:
N = 3, K = 2
A[] = {1, 1, 2}
Output:
2
Explanation:
Splitting the array as {1,1} and {2} is optimal.
This results in a maximum sum subarray of 2.
#########################################################################################

Your Task:
You do not have to take any input or print anything. The task is to complete the function
splitArray() which returns the maximum sum subarray after splitting the array into K
subarrays such that maximum sum subarray is minimum possible.

Expected Time Complexity: O(N*log(sum(arr))).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ N ≤ 105
1 ≤ K ≤ N
1 ≤ arr[i] ≤ 104
"""
#First solution (1.53)
from array import *

class Solution:
    def splitArray(self, arr, N, K):
        def n_partitions(arr,suma):
            """
            Returns no. of subarrays of arr each of them
            accomplishing that its sum is less than "suma"
            """
            curr_sum = 0
            n_partitions = 1
            arr = array('i', arr)
            for i in arr:
                if curr_sum + i <= suma:
                    curr_sum += i
                else:
                    n_partitions += 1
                    curr_sum = i
                    
            return n_partitions
        
        #binary search to get min max sum possible with K partitions
        arr = array('i', arr)
        # The very best partition must isolate the max element
        # to get the minimum possible sum between all
        # the possible partitions of "arr".
        min_sum_subarray = max(arr)
        max_sum_subarray = sum(arr)
        
        l = min_sum_subarray
        r = max_sum_subarray
        while l<=r:
            mid = (l+r)//2
            curr_n_partitions = n_partitions(arr,mid)
            # We can be more demanding with the max possible sum
            # and get more subarrays (closer to K)
            if curr_n_partitions <= K:
                r = mid - 1
            # We must be more flexible in the min possible sum
            # and get fewer subarrays (closer to K)
            else:
                l = mid + 1
        # For every step, we are closer to get K subarrays at
        # the same time we get the max subarray sum we are looking for,
        # that is, the minimum possible with a partition of K subarrays.
        return l
