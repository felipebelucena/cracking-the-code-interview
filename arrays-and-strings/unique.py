from collections import defaultdict

def unique(string):
  """
  Is Unique: Implement an algorithm to determine if a string has all unique characters.
  What if you cannot use additional data structures?
  """
  chars = defaultdict(lambda: 0)
  for char in string:
    chars[char] += 1

  for value in chars.values():
    if value > 1:
      return False
  return True

  def unique_without_extra_data_struct(string):
  """
  Is Unique: Implement an algorithm to determine if a string has all unique characters.
  What if you cannot use additional data structures?
  """
  sorted_string = sorted(string)
  lookup = sorted_string[0]
  for char in sorted_string[1::]:
    if lookup == char:
      return False
    lookup = char

  return True

if __name__ == '__main__':
  assert unique('abc') == True
  assert unique('aabc') == False
  assert unique('a') == True
  assert unique('zhieo234lgashron') == False
  assert unique('zhieo234lgasrn') == True
  assert unique_without_extra_data_struct('abc') == True
  assert unique_without_extra_data_struct('aabc') == False
  assert unique_without_extra_data_struct('a') == True
  assert unique_without_extra_data_struct('zhieo234lgashron') == False
  assert unique_without_extra_data_struct('zhieo234lgasrn') == True
