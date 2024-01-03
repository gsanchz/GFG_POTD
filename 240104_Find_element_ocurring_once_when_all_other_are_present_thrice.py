"""
Given an array of integers arr[] of length N, every element appears thrice
except for one which occurs once. Find that element which occurs once.

############################################################################
Example 1:

Input:
N = 4
arr[] = {1, 10, 1, 1}
Output:
10
Explanation:
10 occurs once in the array while the other
element 1 occurs thrice.
############################################################################
Example 2:

Input:
N = 10
arr[] = {3, 2, 1, 34, 34, 1, 2, 34, 2, 1}
Output:
3
Explanation:
All elements except 3 occurs thrice in the array.
#############################################################################

Your Task:
You do not need to take any input or print anything. You task is to complete
the function singleElement() which takes an array of integers arr and an integer
N which finds and returns the element occuring once in the array.

Constraints:
1 ≤ N ≤ 105
-109 ≤ A[i] ≤ 109

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
"""

#Second solution (first right sol) (0.33)
class Solution:
    def singleElement(self,arr,N):
        arr = sorted(arr)
        window_width = 3
        for i in range(0,N,3):
            start_pos = i
            final_pos = start_pos + window_width
            subarray = arr[start_pos:final_pos]
            max_in_subarray = max(subarray)
            min_in_subarray = min(subarray)
            if max_in_subarray != min_in_subarray:
                try:
                    subarray.remove(max_in_subarray)
                    subarray.remove(max_in_subarray)
                    return min_in_subarray
                except:
                    return max_in_subarray
            else:
                pass
        return arr[N-1]

# Third solution (0.23)
class Solution:
    def singleElement(self,arr,N):
        dicc={}
        for ele in arr:
            if ele in dicc:
                dicc[ele] += 1
            else:
                dicc[ele] = 1
        rev_dic = {value:key for key,value in dicc.items()}
        return rev_dic[1]

# Fourth solution (wrong because takes too much time to run)
class Solution:
    def singleElement(self,arr,N):
        visited = []
        for i in range(0,N):
            if arr[i] not in visited:
                if (arr[i] not in arr[i+1:]):
                    return arr[i]
                visited.append(arr[i])
      
#First solution (wrong because takes too much time to run)
class Solution:
    def singleElement(self,arr, N):
        def take_off(ele,arr):
            arr.remove(ele)
            arr.remove(ele)
            arr.remove(ele)
            return arr
        while len(arr) > 0:
            try:
                ele = arr[0]
                arr = take_off(ele,arr)
            except:
                return ele
