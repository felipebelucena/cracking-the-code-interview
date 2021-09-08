def urlify(chars, str_length):
   """
  Write a method to replace all spaces in a string with '%20'.
  You may assume that the string has sufficient space at the end to hold the additional characters, and that you are
  given the "true" length of the string.
  (Note: If implementing in Java,please use a character array so that you can perform this operation in place.)

  EXAMPLE:
    Input: "Mr John Smith ", 13
    Output: "Mr%20John%20Smith"
  """
  num_of_spaces = len([char for char in chars[:str_length] if char == ' '])
  last_index = str_length + num_of_spaces * 2

  if last_index < len(chars):
    chars[last_index] = '\0'

  for i in range(str_length - 1, -1, -1):
    if chars[i] == ' ':
      chars[last_index - 1] = '0'
      chars[last_index - 2] = '2'
      chars[last_index - 3] = '%'
      last_index -= 3
    else: 
      chars[last_index - 1] = chars[i]
      last_index -= 1

  return ''.join(chars).split('\0')[0]



if __name__ == '__main__':
  assert urlify(list('Mr John Smith      '), 13) == 'Mr%20John%20Smith'
  assert urlify(list('nospaces'), 8) == 'nospaces'
  assert urlify(list('Mr  Two Spaces      '), 14) == 'Mr%20%20Two%20Spaces'
  assert urlify(list('spaceAtTheEnd     '), 14) == 'spaceAtTheEnd%20'
  assert urlify(list(' spaceAtTheBegining  '), 19) == '%20spaceAtTheBegining'
