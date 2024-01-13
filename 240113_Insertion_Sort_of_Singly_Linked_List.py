'''
INSERTION SORT ALGORITHM

Given a singly linked list, sort the list (in ascending order) using insertion sort algorithm.

##############################################################################################
Example 1:

Input:
N = 10
Linked List = 30->23->28->30->11->14->
              19->16->21->25 
Output : 
11 14 16 19 21 23 25 28 30 30 
Explanation :
The resultant linked list is sorted.
##############################################################################################
Example 2:

Input : 
N = 7
Linked List=19->20->16->24->12->29->30 
Output : 
12 16 19 20 24 29 30 
Explanation : 
The resultant linked list is sorted.
##############################################################################################
Your task:
You don't need to read input or print anything. Your task is to complete the function
insertionSort() which takes the head of the linked list, sorts the list using insertion sort
algorithm and returns the head of the sorted linked list.
 
Expected Time Complexity : O(n2)
Expected Auxiliary Space : O(1)
 
Constraints:
0 <= n <= 5*103
'''


'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
            
    def insertionSort(self, head):

        #def Node_to_list(node):
            #lista = []
            #while node:
                #lista.append(node.data)
                #node = node.next
            #return [lista[0]] + ['|'] + lista[1:]
            
        #print(Node_to_list(head))
        if not head or not head.next: # 0 or 1 element head
            return head
        
        dummy = Node(-1)
        dummy.next = head

        current = head #[>30,23,28,30,...]
        i = 1
        while current.next:

            if current.next.data < current.data:
                #print(f'{i} disordered')
                
                ####################################################################
                # We point to the second element (i.e we take current.next)
                # So the new first element (23) is smaller than the old first (30)
                ####################################################################
                to_insert = current.next #[>23,28,30,...]
                #print(f'Loop={i},to_insert={Node_to_list(to_insert)}')
                
                ####################################################################
                # We point to the first element (the bigger element)
                # and forget the second element with .next.next
                ####################################################################
                #print(f'Loop={i},current={Node_to_list(current)}')
                current.next = current.next.next
                #current=[30,[28,30,...]]=head -> dummy = [-1 head]
                
                #print(f'Loop={i},current={Node_to_list(current)}')
                #print(f'Loop={i},head={Node_to_list(current)}')
                #print(f'Loop={i},dummy={Node_to_list(dummy)}')
                
                ####################################################################
                # A copy of dummy. Dummy always point to the start
                ####################################################################
                ptr = dummy #= [-1 current] = [>-1,30,28,30,...]
                
                ####################################################################
                # Move till we reach the right position to insert a
                # tail of elements that are bigger than first element of to_insert
                # so the first element of ptr is the biggest smaller element
                ####################################################################
                #print(f'Loop={i},ptr_bef_desp={Node_to_list(ptr)}')
                #desp = 0
                while ptr.next and ptr.next.data < to_insert.data:
                    ptr = ptr.next
                    #desp +=1
                #print(f'Loop={i},ptr_{desp}={Node_to_list(ptr)}')
                
                to_insert.next = ptr.next #[23,[30,28,30,...]]
                #print(f'Loop={i},to_insert={Node_to_list(to_insert)}')
                
                ####################################################################
                # dummy pointer is the same as ptr pointer so changes in ptr are
                # in dummy too: dummy = [...,ptr.data,ptr.next=to_insert]
                ####################################################################
                ptr.next = to_insert #[-1,[23,30,28,30...]]
                #print(f'Loop={i},ptr={Node_to_list(ptr)}')
                
            else:
                #print(f'{i} not disordered')
                #print(f'Loop={i},current={Node_to_list(current)}')
                current = current.next
                #print(f'Loop={i},new_current={Node_to_list(current)}')
            #print(f'Loop={i},dummy={Node_to_list(dummy)}')
            #i+=1

        return dummy.next


"""
Example with [30, '|', 23, 28, 30, 11, 14, 19, 16, 21, 25]

1 disordered
Loop=1,to_insert=[23, '|', 28, 30, 11, 14, 19, 16, 21, 25]
Loop=1,current=[30, '|', 23, 28, 30, 11, 14, 19, 16, 21, 25]
Loop=1,current=[30, '|', 28, 30, 11, 14, 19, 16, 21, 25]
Loop=1,head=[30, '|', 28, 30, 11, 14, 19, 16, 21, 25]
Loop=1,dummy=[-1, '|', 30, 28, 30, 11, 14, 19, 16, 21, 25]
Loop=1,ptr_bef_desp=[-1, '|', 30, 28, 30, 11, 14, 19, 16, 21, 25]
Loop=1,desp=0,ptr_desp=[-1, '|', 30, 28, 30, 11, 14, 19, 16, 21, 25]
Loop=1,to_insert=[23, '|', 30, 28, 30, 11, 14, 19, 16, 21, 25]
Loop=1,ptr=[-1, '|', 23, 30, 28, 30, 11, 14, 19, 16, 21, 25]
Loop=1,dummy=[-1, '|', 23, 30, 28, 30, 11, 14, 19, 16, 21, 25]

2 disordered
Loop=2,to_insert=[28, '|', 30, 11, 14, 19, 16, 21, 25]
Loop=2,current=[30, '|', 28, 30, 11, 14, 19, 16, 21, 25]
Loop=2,current=[30, '|', 30, 11, 14, 19, 16, 21, 25]
Loop=2,head=[30, '|', 30, 11, 14, 19, 16, 21, 25]
Loop=2,dummy=[-1, '|', 23, 30, 30, 11, 14, 19, 16, 21, 25]
Loop=2,ptr_bef_desp=[-1, '|', 23, 30, 30, 11, 14, 19, 16, 21, 25]
Loop=2,desp=1,ptr_desp=[23, '|', 30, 30, 11, 14, 19, 16, 21, 25]
Loop=2,to_insert=[28, '|', 30, 30, 11, 14, 19, 16, 21, 25]
Loop=2,ptr=[23, '|', 28, 30, 30, 11, 14, 19, 16, 21, 25]
Loop=2,dummy=[-1, '|', 23, 28, 30, 30, 11, 14, 19, 16, 21, 25]

3 not disordered
Loop=3,current=[30, '|', 30, 11, 14, 19, 16, 21, 25]
Loop=3,new_current=[30, '|', 11, 14, 19, 16, 21, 25]
Loop=3,dummy=[-1, '|', 23, 28, 30, 30, 11, 14, 19, 16, 21, 25]

4 disordered
Loop=4,to_insert=[11, '|', 14, 19, 16, 21, 25]
Loop=4,current=[30, '|', 11, 14, 19, 16, 21, 25]
Loop=4,current=[30, '|', 14, 19, 16, 21, 25]
Loop=4,head=[30, '|', 14, 19, 16, 21, 25]
Loop=4,dummy=[-1, '|', 23, 28, 30, 30, 14, 19, 16, 21, 25]
Loop=4,ptr_bef_desp=[-1, '|', 23, 28, 30, 30, 14, 19, 16, 21, 25]
Loop=4,desp=0,ptr_desp=[-1, '|', 23, 28, 30, 30, 14, 19, 16, 21, 25]
Loop=4,to_insert=[11, '|', 23, 28, 30, 30, 14, 19, 16, 21, 25]
Loop=4,ptr=[-1, '|', 11, 23, 28, 30, 30, 14, 19, 16, 21, 25]
Loop=4,dummy=[-1, '|', 11, 23, 28, 30, 30, 14, 19, 16, 21, 25]

5 disordered
Loop=5,to_insert=[14, '|', 19, 16, 21, 25]
Loop=5,current=[30, '|', 14, 19, 16, 21, 25]
Loop=5,current=[30, '|', 19, 16, 21, 25]
Loop=5,head=[30, '|', 19, 16, 21, 25]
Loop=5,dummy=[-1, '|', 11, 23, 28, 30, 30, 19, 16, 21, 25]
Loop=5,ptr_bef_desp=[-1, '|', 11, 23, 28, 30, 30, 19, 16, 21, 25]
Loop=5,desp=1,ptr_desp=[11, '|', 23, 28, 30, 30, 19, 16, 21, 25]
Loop=5,to_insert=[14, '|', 23, 28, 30, 30, 19, 16, 21, 25]
Loop=5,ptr=[11, '|', 14, 23, 28, 30, 30, 19, 16, 21, 25]
Loop=5,dummy=[-1, '|', 11, 14, 23, 28, 30, 30, 19, 16, 21, 25]

6 disordered
Loop=6,to_insert=[19, '|', 16, 21, 25]
Loop=6,current=[30, '|', 19, 16, 21, 25]
Loop=6,current=[30, '|', 16, 21, 25]
Loop=6,head=[30, '|', 16, 21, 25]
Loop=6,dummy=[-1, '|', 11, 14, 23, 28, 30, 30, 16, 21, 25]
Loop=6,ptr_bef_desp=[-1, '|', 11, 14, 23, 28, 30, 30, 16, 21, 25]
Loop=6,desp=2,ptr_desp=[14, '|', 23, 28, 30, 30, 16, 21, 25]
Loop=6,to_insert=[19, '|', 23, 28, 30, 30, 16, 21, 25]
Loop=6,ptr=[14, '|', 19, 23, 28, 30, 30, 16, 21, 25]
Loop=6,dummy=[-1, '|', 11, 14, 19, 23, 28, 30, 30, 16, 21, 25]

7 disordered
Loop=7,to_insert=[16, '|', 21, 25]
Loop=7,current=[30, '|', 16, 21, 25]
Loop=7,current=[30, '|', 21, 25]
Loop=7,head=[30, '|', 21, 25]
Loop=7,dummy=[-1, '|', 11, 14, 19, 23, 28, 30, 30, 21, 25]
Loop=7,ptr_bef_desp=[-1, '|', 11, 14, 19, 23, 28, 30, 30, 21, 25]
Loop=7,desp=2,ptr_desp=[14, '|', 19, 23, 28, 30, 30, 21, 25]
Loop=7,to_insert=[16, '|', 19, 23, 28, 30, 30, 21, 25]
Loop=7,ptr=[14, '|', 16, 19, 23, 28, 30, 30, 21, 25]
Loop=7,dummy=[-1, '|', 11, 14, 16, 19, 23, 28, 30, 30, 21, 25]

8 disordered
Loop=8,to_insert=[21, '|', 25]
Loop=8,current=[30, '|', 21, 25]
Loop=8,current=[30, '|', 25]
Loop=8,head=[30, '|', 25]
Loop=8,dummy=[-1, '|', 11, 14, 16, 19, 23, 28, 30, 30, 25]
Loop=8,ptr_bef_desp=[-1, '|', 11, 14, 16, 19, 23, 28, 30, 30, 25]
Loop=8,desp=4,ptr_desp=[19, '|', 23, 28, 30, 30, 25]
Loop=8,to_insert=[21, '|', 23, 28, 30, 30, 25]
Loop=8,ptr=[19, '|', 21, 23, 28, 30, 30, 25]
Loop=8,dummy=[-1, '|', 11, 14, 16, 19, 21, 23, 28, 30, 30, 25]

9 disordered
Loop=9,to_insert=[25, '|']
Loop=9,current=[30, '|', 25]
Loop=9,current=[30, '|']
Loop=9,head=[30, '|']
Loop=9,dummy=[-1, '|', 11, 14, 16, 19, 21, 23, 28, 30, 30]
Loop=9,ptr_bef_desp=[-1, '|', 11, 14, 16, 19, 21, 23, 28, 30, 30]
Loop=9,desp=6,ptr_desp=[23, '|', 28, 30, 30]
Loop=9,to_insert=[25, '|', 28, 30, 30]
Loop=9,ptr=[23, '|', 25, 28, 30, 30]
Loop=9,dummy=[-1, '|', 11, 14, 16, 19, 21, 23, 25, 28, 30, 30]
11 14 16 19 21 23 25 28 30 30  
"""
