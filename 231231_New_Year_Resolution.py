"""
As the clock struck midnight on New Year's Eve, Geek bid farewell to the wasted
moments of 2023, realizing the untapped potential of GFG's Problem of the Day.

His 2024 resolution: Solve POTD every day.

Eager to earn coins for GFG Merchandise, Geek faces new rules:

Earning Coin: Geek can accumulate coins[i] by solving the POTD on the ith day,
where 1 <= coins[i] <= 2024 and the sum of coins <= 2024.
Merchandise Eligibility: To purchase merchandise, the coins earned must be
divisible by 20 or 24, or precisely equal to 2024.
Geek's resolutions often fades over time. Realistically, he can only commit to
active participation for N (where N ≤ 366) days. Given the value of N and number
of coins associated with each POTD, can Geek strategically solve some (or all)
POTDs to become eligible for redeeming merchandise?

#######################################################
Example 1:

Input:
N = 8
coins = [5, 8, 9, 10, 14, 2, 3, 5]

Output: 1

Explanation:
Geek can fulfill the criteria in many ways.
One such way is to solve POTD on 4th and 5th day.
Another way is to solve POTD on 1st, 4th and 8th day.
#######################################################
Example 2:

Input:
N = 5
coins = [1, 2, 3, 4, 5]

Output: 0

Explanation: There is no way Geek can become eligible.
#######################################################

Your Task: 
You don't need to read input or print anything. Complete the function isPossible()
which takes n and coins[ ] as input parameters and returns a boolean value.

Expected Time Complexity: O(N*(Sum of coins))
Expected Auxiliary Space: O(N*(Sum of coins))

Constraints:
1 <= N <= 366
1 <= coins[i] <= 2024
1 <= Sum of coins <=  2024
"""

###############################################################################
# 1 out of 3 version (0.11s)
###############################################################################
from typing import List

class Solution:
    
    def isPossible(self, N : int, coins : List[int]) -> bool:
        
        def check(i : int, suma : int, coins : List[int]) -> bool:
            if (suma > 0) and ((suma%20 == 0) or (suma%24 == 0) or (suma == 2024)):
                return True
            if i >= len(coins):
                return False
        
            return check(i+1,suma,coins) or check(i+1,suma+coins[i],coins)
            
        return check(0,0,coins)
      
###############################################################################
# 2 out of 3 version (0.21s)
###############################################################################
from typing import List

class Solution:
    
    def isPossible(self, N : int, coins : List[int]) -> bool:
        # sum_of_coins <= 2024
        visit_sums = [0] * 2024
        
        def check(i : int, suma : int, coins : List[int]) -> bool:
            if (suma > 0) and ((suma%20 == 0) or (suma%24 == 0) or (suma == 2024)):
                return True
            if i >= len(coins):
                return False
            #Avoid recalculate suma conditions by checking in a list
            check_sum_bool = visit_sums[suma]
            if check_sum_bool != 0:
                return check_sum_bool
        
            visit_sums[suma] = check(i+1,suma,coins) or check(i+1,suma+coins[i],coins)
            return visit_sums[suma]
        return check(0,0,coins)
      
###############################################################################
# 3 out of 3 version (0.64s)
###############################################################################

from typing import List

class Solution:
    
    def isPossible(self, N : int, coins : List[int]) -> bool:
        #sum_of_coins <=2024
        suma_check = [True if ((suma > 0) and
                        ((suma%20 == 0) or (suma%24 == 0) or (suma == 2024)))
                        else False for suma in range(2025)]
        
        def check(i : int, suma : int, coins : List[int]) -> bool:
            if suma_check[suma]:
                return True
            if i >= len(coins):
                return False
            return check(i+1,suma,coins) or check(i+1,suma+coins[i],coins)
            
        return check(0,0,coins)
