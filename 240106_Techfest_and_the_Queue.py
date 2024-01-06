"""
A Techfest is underway, and each participant is given a ticket with a unique number.
Organizers decide to award prize points to everyone who has a ticket ID between a and b
(inclusive). The points given to a participant with ticket number x will be the sum of
powers of the prime factors of x.

For instance, if points are to be awarded to a participant with ticket number 12, the
amount of points given out will be equal to the sum of powers in the prime factorization
of 12 (22 × 31), which will be 2 + 1 = 3.

Given a and b, determine the sum of all the points that will be awarded to the participants
with ticket numbers between a and b (inclusive).

###########################################################################################
Example 1:

Input: 
a = 9
b = 12
Output: 
8
Explanation: 
For 9, prime factorization is:32 
So, sum of the powers of primes is: 2
For 10, prime factorization is : 21x51 
So, sum of the powers of primes is: 2
For 11, prime factorization is : 111 
So, sum of the powers of primes is: 1
For 12, prime factorization is : 22x 31 
So, sum of powers of primes is: 3
Therefore the total sum is 2+2+1+3=8.
###########################################################################################
Example 2:

Input: 
a = 24, b = 27
Output: 
11
Explanation: 
For 24, prime factorization is: 23x31 
So, sum of the powers of primes is: 4
For 25, prime factorization is : 52 
So, sum of the powers of primes is: 2
For 26, prime factorization is : 131x21 
So, sum of the powers of primes is: 2
For 27, prime factorization is : 33  
So, sum of powers of primes is: 3
Therefore the total sum is 4+2+2+3=11.
###########################################################################################

Your Task:
You don't need to read or print anything. Your task is to complete the function sumOfPowers() which takes a and b as input parameters and returns the sum of the power of primes that occur in prime factorization of the numbers between a to b (inclusive).

Expected Time Complexity: O( b*log(b) )
Expected Space Complexity: O( b*log(b) )

Constraints:
1 <= a <= b <= 2x105
1 <= b-a <= 105
"""

from typing import List

#Seventh and unique right solution (2.22)
from array import *

def sumOfPowers(a, b):
    def erathostenes_sieve(n,m):
        n_factors = array('i',[0] * (m + 1))
        for i in range(2, m + 1):
            if n_factors[i] == 0:  # i is prime
                start = i * ((n + i - 1) // i)
                for j in range(i*2, start, i):
                    # Only mark composite nums less than n with 1
                    # we don't count their number of factors
                    n_factors[j] = 1
                for j in range(start, m + 1, i):
                    aux = j
                    # Only loops to count exact no. of factors
                    # if the number is inside the [n,m] interval
                    while aux%i == 0:
                        n_factors[j] += 1
                        aux = aux//i
        return n_factors

    factors_till_b = erathostenes_sieve(a,b)
    prize = sum(factors_till_b[a:b+1])
    return prize

#WORK HISTORY

#Sixth solution (takes too much time)
from array import *

class Solution:
    def sumOfPowers(self, a : int, b : int) -> int:
        def erathostenes_sieve(m):
            n_factors = array('i', [0] * (m + 1))
            for i in range(2, m + 1):
                if n_factors[i] == 0:  # i is prime
                    for j in range(i, m + 1, i):
                        aux = j
                        while aux%i == 0:
                            n_factors[j] += 1
                            aux = aux//i
            return n_factors
        
        factors_till_b = erathostenes_sieve(b)
        prize = sum(factors_till_b[a:b+1])
        return prize

#Fifth solution (takes too much time)
class Solution:
    def sumOfPowers(self, a : int, b : int) -> int:
        def erathostenes_sieve(m):
            n_factors = [0] * (m + 1)
            for i in range(2, m + 1):
                if n_factors[i] == 0:  # i is prime
                    for j in range(i, m + 1, i):
                        aux = j
                        while aux%i == 0:
                            n_factors[j] += 1
                            aux = aux/i
            return n_factors
          
        factors_till_b = erathostenes_sieve(b)
        prize = sum(factors_till_b[a:b+1])
        return prize

#First solution (takes too much time)
class Solution:
    def sumOfPowers(self, a : int, b : int) -> int:
        def n_primes(m):
            count = 0
            for i in range(2,int(m**(1/2))+1):
                while m%i == 0:
                    count += 1
                    m = m/i
            if m > 1: #m is a prime
                count += 1
            return count
            
        prize = 0
        for j in range(a,b+1):
            prize += n_primes(j)
        return prize

# Second more time-complex solution
class Solution:
    def sumOfPowers(self, a : int, b : int) -> int:
        def n_primes(m,dicc):
            count = 0
            for i in range(2,int(m**(1/2))+1):
                if dicc.get(m) != None:
                    count += dicc[m]
                    m = 1
                    break
                else:
                    while m%i == 0:
                        count += 1
                        m = m/i
            if m > 1: #m is a prime
                count += 1
            return count
            
        prize = 0
        dicc_prize = {}
        for j in range(a,b+1):
            dicc_prize[j] = n_primes(j,dicc_prize)
            prize += dicc_prize[j]

# Third more time-complex solution
class Solution:
    def sumOfPowers(self, a : int, b : int) -> int:
        def sqrt_int(number): #To avoid OverflowError with large ints when sqrt
            
            if number == 0 or number == 1:
                return number
        
            start, end = 0, number
            while start <= end:
                mid = (start + end) // 2
                sqrt_mid = mid * mid
        
                if sqrt_mid == number:
                    return mid
                elif sqrt_mid < number:
                    start = mid + 1
                    ans = mid
                else:
                    end = mid - 1
        
            return ans
        
        def n_primes(m):
            count = 0
            for i in range(2,sqrt_int(m)+1):
                while m%i == 0:
                    count += 1
                    m = m//i
            if m > 1: #m is a prime
                count += 1
            return count
            
        prod = 1
        for j in range(a,b+1):
            prod *= j
        return n_primes(prod)

# Fourth solution more time-complex solution

class Solution:
    def sumOfPowers(self, a : int, b : int) -> int:
        
        def n_primes(m):
            count = 0
            for i in range(2,int(m**(1/2))+1):
                while m%i == 0:
                    count += 1
                    m = m//i
            if m > 1: #m is a prime
                count += 1
            return count
            
        prod = 1
        prod_list = []
        for j in range(a,b+1):
            prod *= j
            if prod > 10**308: # To avoid OverflowError when sqrt of int
                prod = prod/j
                prod_list.append(prod)
                prod = j
        prod_list.append(prod)
        points = 0
        for prod in prod_list:
            points += n_primes(prod)
        return points
