"""
Given an array of integers nums and a number k, write a function that returns true
if given array can be divided into pairs such that sum of every pair is divisible by k.
#######################################################################################
Example 1 :

Input : 
nums = [9, 5, 7, 3]
k = 6
Output: 
True
Explanation: 
{(9, 3), (5, 7)} is a 
possible solution. 9 + 3 = 12 is divisible
by 6 and 7 + 5 = 12 is also divisible by 6.
########################################################################################
Example 2:

Input : 
nums = [4, 4, 4]
k = 4
Output: 
False
Explanation: 
You can make 1 pair at max, leaving a single 4 unpaired.
#######################################################################################

Your Task:
You don't need to read or print anything. Your task is to complete the function canPair()
which takes array nums and k as input parameter and returns true if array can be divided
into pairs such that sum of every pair is divisible by k otherwise returns false.

Expected Time Complexity: O(n)
Expected Space Complexity : O(n)

Constraints:
1 <= length( nums ) <= 105
1 <= numsi <= 105
1 <= k <= 105
"""

# My second solution (0.22)
class Solution:
    def canPair(self, nuns, k):
        if len(nuns)%2 == 1:
            return False
	rem_dict = dict(zip(range(k),[0]*k))
	for nun in nuns:
	    rem_dict[nun%k] += 1
	if rem_dict[0]%2 == 1:
	    return False
	for j in range(1,k//2):
	    if rem_dict[j] != rem_dict[k-j]:
	        return False
	return True

# Third solution (0.32) worst performance than the second.
# I don't create all the possible keys, instead I create the minimum neccesary.
class Solution:
    def canPair(self, nuns, k):
        if len(nuns)%2 == 1:
            return False
        rem_dict = {0:0}
        for nun in nuns:
            if rem_dict.get(nun%k) == None:
                rem_dict[nun%k] = 1
            else:
                rem_dict[nun%k] += 1
        if rem_dict[0]%2 == 1:
            return False
        for j in range(1,k//2):
            if rem_dict.get(j) != rem_dict.get(k-j):
                return False
        return True


# With numpy (first solution, no admissible)
import numpy as np

class Solution:
    def canPair(self, nuns, k):
        if len(nuns)%2 == 1:
	    return False
	nuns_div = np.array([nun%k for nun in nuns])
	if (nuns_div == 0).sum() %2 == 1:
	    return False
        for j in range(1, k//2 + 1):
	    if (nuns_div == j).sum() != (nuns_div == k-j).sum()
		return False
        return True
