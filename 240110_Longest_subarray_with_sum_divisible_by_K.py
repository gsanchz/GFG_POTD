"""
Given an array arr containing N integers and a positive integer K, find the length
of the longest sub array with sum of the elements divisible by the given value K.

#####################################################################################
Example 1:

Input:
N = 6, K = 3
arr[] = {2, 7, 6, 1, 4, 5}
Output: 
4
Explanation:
The subarray is {7, 6, 1, 4} with sum 18, which is divisible by 3.
####################################################################################
Example 2:

Input:
N = 7, K = 3
arr[] = {-2, 2, -5, 12, -11, -1, 7}
Output: 
5
Explanation:
The subarray is {2,-5,12,-11,-1} with sum -3, which is divisible by 3.
###################################################################################

Your Task:
The input is already taken care of by the driver code. You only need to
complete the function longSubarrWthSumDivByK() that takes an array arr,
sizeOfArray n and a  positive integer K, and returns the length of the
longest subarray which has sum divisible by K. 

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= N <= 105
1 <= K <= 109
-109 <= A[i] <= 109 
"""

#Second try (0.25)
class Solution:
	def longSubarrWthSumDivByK (self, arr, n, K) :
        dicc = {0:-1}
        current_sum_rem, ans = 0, 0
        for pos, val in enumerate(arr):
            current_sum_rem= (current_sum_rem+val)%K
            if current_sum_rem not in dicc:
                dicc[current_sum_rem] = pos
            else:
                ans = max(ans, pos - dicc[current_sum_rem])
        return ans
  
# First try (too slow > 1.5)
class Solution:
  def longSubarrWthSumDivByK (self, arr, n, K) :
      arr_suma_remainder = sum(arr)%K
      if arr_suma_remainder == 0:
          return n
      for head,tail in [(x, l - x) for l in range(1, len(arr)) for x in range(l + 1)]:
          head_remainder = sum(arr[:head])%K
          tail_remainder = sum(arr[n-tail:])%K
          if arr_suma_remainder - (head_remainder + tail_remainder) == 0:
              return n - (head + tail)
      return 0
