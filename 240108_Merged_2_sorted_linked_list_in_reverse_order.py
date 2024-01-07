"""
Given two linked lists of size N and M, which are sorted in non-decreasing order.
The task is to merge them in such a way that the resulting list is in non-increasing order.

####################################################################################################
Example 1:

Input:
N = 2, M = 2
list1 = 1->3
list2 = 2->4
Output:
4->3->2->1
Explanation:
After merging the two lists in non-increasing order, we have new lists as 4->3->2->1.
###################################################################################################
Example 2:

Input:
N = 4, M = 3
list1 = 5->10->15->40 
list2 = 2->3->20
Output:
40->20->15->10->5->3->2
Explanation:
After merging the two lists in non-increasing order, we have new lists as 40->20->15->10->5->3->2.
####################################################################################################

Your Task:
The task is to complete the function mergeResult() which takes reference to the heads of
both linked list and returns the pointer to the merged linked list.

Expected Time Complexity : O(N+M)
Expected Auxiliary Space : O(1)

Constraints:
0 <= N, M <= 104
"""

'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
# (0.9)
class Solution:
    def mergeResult(self,h1,h2):
        # There's no elements in list (Node.data) h1
        if not h1:
            temp = h2
            temp_bis = h2
        # There's no elements in list (Node.data) h2
        if not h2:
            temp = h1
            temp_bis = h1
        
        # If there are elements in both h1 and h2
        # we make a wider Node object with h1 and h2 elements
        if h1 and h2:
            temp = h1
            while temp.next:
                temp = temp.next
            temp.next = h2 # attach last node of 1st list to second list
            temp = h1
            temp_bis = h1
        
        # Collect node values (temp node) in a list
        node_values = []
        temp = temp
        while temp:
            node_values.append(temp.data)
            temp = temp.next
        
        # Sort in reverse order
        node_values.sort(reverse=True)
        
        # Update the temp_bis node values with the ones in node_values
        temp = temp_bis
        for value in node_values:
            temp.data = value
            temp = temp.next
        return temp_bis
        
