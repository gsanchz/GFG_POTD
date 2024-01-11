# Second solution (0.28)

class Solution:

    def removeKdigits(self, S, k):
        stack = []
        for e in S:
            # We remove bigger n from array tail
            while stack and k > 0 and e < stack[-1]:
                k -= 1 # Till k reaches 0, i.e., we remove k times
                stack.pop()
            # And replace with a smaller n
            stack.append(e)
        # Finally, we got an ascendent-digit number like '123456'
        
        # If less than k n in S were removed, we remove n at the tail
        # till we reach k n removed. For example, '12345'.
        while k > 0:
            stack.pop()
            k -= 1
        
        # We ignore 0's at the head of the string
        i = 0
        while i < len(stack) and stack[i] == '0':
            i += 1
        # But could be that the given S has (len(S) - k) zeros
        if i == len(stack):
            return "0"
        # Once we know where the first non-zero digit starts, we get the ans
        return "".join(stack[i:])

# First solution (wrong solution because I considered digits could be reordered)
class Solution:

    def removeKdigits(self, S, K):
        len_str = len(S)
        if len_str == K:
            return 0
        
        digit_dic = dict(zip(range(0,10),[0]*10))
        for s in S:
            digit_dic[int(s)] += 1
        
        ans = ''
        for n,i in digit_dic.items():
            ans += str(n) * i
            if len(ans) > len_str - K:
                break
        end = len_str-int(K)
        return int(ans[:end])
