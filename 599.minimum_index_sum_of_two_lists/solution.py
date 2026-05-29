class Solution:
  def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
    index = {name: i for i, name in enumerate(list1)}

    min_sum = float('inf')
    ans = []

    for j, name in enumerate(list2):
      if name in index:
        total = index[name] + j

        if total < min_sum:
          min_sum = total
          ans = [name]
        elif total == min_sum:
          ans.append(name)

    return ans