"""
Given a string S consisting of the characters 0, 1 and 2. Your task is to find the
length of the smallest substring of string S that contains all the three characters
0, 1 and 2. If no such substring exists, then return -1.

################################################################################
Example 1:

Input:
S = 01212
Output:
3
Explanation:
The substring 012 is the smallest substring
that contains the characters 0, 1 and 2.
################################################################################
Example 2:

Input: 
S = 12121
Output:
-1
Explanation: 
As the character 0 is not present in the
string S, therefor no substring containing
all the three characters 0, 1 and 2
exists. Hence, the answer is -1 in this case.
################################################################################

Your Task:
Complete the function smallestSubstring() which takes the string S as input, and
returns the length of the smallest substring of string S that contains all the
three characters 0, 1 and 2.

Expected Time Complexity: O( length( S ) )
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ length( S ) ≤ 105
All the characters of String S lies in the set {'0', '1', '2'}
"""

#Second solution (0.04)

class Solution:
    def smallestSubstring(self,S):
        min_width = 3
        len_S = len(S)
        if len_S < min_width:
            return -1
        for sum_width in range(len_S - min_width + 1):
            window_width = 3 + sum_width
            for start_pos in range(len_S - window_width + 1):
                final_pos = start_pos + window_width
                substring = S[start_pos:final_pos]
                if ('0' in substring) and ('1' in substring) and ('2' in substring):
                    return window_width
                else:
                    pass
        return -1

#First solution (2.54)
class Solution:
    def smallestSubstring(self, S):
        str_dic = {'0':0,'1':0,'2':0}
        pos_dic = {'0':0,'1':0,'2':0}
        len_list = []
        for pos,s in enumerate(S):
            str_dic[s] += 1
            pos_dic[s] = pos
            if (str_dic['0'] > 0) and (str_dic['1'] > 0) and (str_dic['2'] > 0):
                length = max(abs(pos_dic['0']-pos_dic['1']),
                            abs(pos_dic['0']-pos_dic['2']),
                            abs(pos_dic['1']-pos_dic['2'])) + 1
                len_list.append(length)
                str_dic = dict(zip(str_dic.keys(),[0]*3))
        if len(len_list) == 0:
            return -1
        return min(len_list)
