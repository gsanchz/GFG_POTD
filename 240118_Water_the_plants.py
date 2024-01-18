# First solution (too much run time)
class Solution:
  def min_sprinklers(self,gallery, n):
      def turn_splinker(i,watered_list):
          if i == n:
              if watered_list == list(range(n)):
                  return 0
              else:
                  return n + 1
          # Not turn splinker
          not_turn = turn_splinker(i+1,watered_list)
          if gallery[i] == -1:
              return not_turn
          # Turn splinker
          if len(watered_list) > 0:
              min_watered = max(0,i-gallery[i],max(watered_list)+1)
          else:
              min_watered = max(0,i-gallery[i])
          max_watered = min(n,i+gallery[i])
          turn_watered_list = watered_list + list(range(min_watered,max_watered))
          print(turn_watered_list)
          turn = turn_splinker(i+1,turn_watered_list)
          return min(not_turn,1+turn)
      
      ans = turn_splinker(0,[])
      if ans > n:
          return -1
      return ans
