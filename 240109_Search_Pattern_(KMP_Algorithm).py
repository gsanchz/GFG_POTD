"""
Given two strings, one is a text string, txt and other is a pattern string, pat.
The task is to print the indexes of all the occurences of pattern string in the
text string. Use one-based indexing while returing the indices. 
Note: Return an empty list incase of no occurences of pattern. Driver will print
-1 in this case.

#######################################################################################
Example 1:

Input:
txt = "geeksforgeeks"
pat = "geek"
Output: 
1 9
Explanation: 
The string "geek" occurs twice in txt, one starts are index 1 and the other at index 9.
#######################################################################################
Example 2:

Input: 
txt = "abesdu"
pat = "edu"
Output: 
-1
Explanation: 
There's not substring "edu" present in txt.
######################################################################################

Your Task:
You don't need to read input or print anything. Your task is to complete the function
search() which takes the string txt and the string pat as inputs and returns an array
denoting the start indices (1-based) of substring pat in the string txt. 

Expected Time Complexity: O(|txt|).
Expected Auxiliary Space: O(|txt|).

Constraints:
1 ≤ |txt| ≤ 105
1 ≤ |pat| < |S|
Both the strings consists of lowercase English alphabets.
"""

# First solution (2.22)
class Solution:
    def search(self, pat, txt):
        if pat not in txt:
            return []
            
        pat_len = len(pat)
        txt_len = len(txt)
        pos_list = []
        for i in range(txt_len - pat_len + 1):
            if txt[i:i+pat_len] == pat:
                pos_list.append(i+1)
        return pos_list
# Second solution (2.53) Knuth-Morris-Pratt Algorithm

class Solution:    
    def search(self, pat, txt):
        # Auxiliary function to calculate lps
        def computeLPSArray(pat, M, lps):
          """
          
          Returns: list of len = len(pat) which values indicate the len
          of the substring of pat[:i+1] that is prefix and suffix
          at the same time. For example:
          pat = "ABABCABAB" has lps = [0, 0, 1, 2, 0, 1, 2, 3, 4] because
          lps[2] = 1, i.e. pat[:3] has prefix = "A" = suffix and len("A") = 1
          lps[3] = 2, i.e. pat[:4] = "ABAB" has prefix = "AB" = suffix of len 2
          
          """
            length = 0
            i = 1
        
            while i < M:
                if pat[i]== pat[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length-1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

      # Continue "search" function
    	M = len(pat)
      N = len(txt)
  
      lps = [0]*M
      j = 0
  
      computeLPSArray(pat, M, lps)
      
      pos_list = []
      i = 0
      while i < N:
          if pat[j] == txt[i]:
              i += 1
              j += 1
  
          if j == M:
              pos_list.append(i - j + 1)
              j = lps[j - 1]
          
          elif i < N and pat[j] != txt[i]:

              if j != 0:
                  j = lps[j-1]
              else:
                  i += 1
          
      return pos_list
