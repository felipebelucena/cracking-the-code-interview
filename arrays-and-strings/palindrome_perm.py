from collections import defaultdict

def palindrome_perm(str):
  """
  Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin­ drome.
  A palindrome is a word or phrase that is the same forwards and backwards.
  A permutation is a rearrangement of letters.
  The palindrome does not need to be limited to just dictionary words.
  
  EXAMPLE:
    Input: Tact Coa
    Output: True (permutations: "taco cat", "atco eta", etc.)
  """
  chars_map = defaultdict(lambda: 0)
  for char in str:
    if char != ' ':
      chars_map[char.lower()] += 1
  
  odds = 0
  for freq in chars_map.values():
    if freq % 2 != 0:
      odds += 1
    if odds > 1:
      return False
  return True

if __name__ == '__main__':
  assert palindrome_perm('Tact Coa') == True
  assert palindrome_perm('abab') == True
  assert palindrome_perm('aabb abc cab') == True
  assert palindrome_perm('xyz') == False
