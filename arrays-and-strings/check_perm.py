from collections import defaultdict

def check_perm(str1, str2):
  """
  Check Permutation: Given two strings,write a method to decide if one is a permutation of the other.
  """
  if len(str1) != len(str2):
    return False
  
  chars_map = defaultdict(lambda: 0)
  for char in str1:
    chars_map[char] += 1

  for char in str2:
    chars_map[char] -= 1
    if chars_map[char] < 0:
      return False

  return True


if __name__ == '__main__':
  assert check_perm('abc', 'cba') == True
  assert check_perm('a', 'a') == True


  assert check_perm('ba', 'ab') == True
  assert check_perm('dad', 'ded') == False
  assert check_perm('roma', 'amor') == True
  assert check_perm('bbdede', 'ddbebe') == True
  assert check_perm('bbdede', 'ddbebf') == False
  assert check_perm('wyz', 'lkouh') == False
