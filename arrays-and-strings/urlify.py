def urlify(chars, str_length):
  last_index = len(chars) - 1

  for i in range(str_length - 1, -1, -1):
    if chars[i] != ' ':
      chars[last_index] = chars[i]
      last_index -= 1
    else: 
      chars[last_index] = '0'
      chars[last_index - 1] = '2'
      chars[last_index - 2] = '%'
      last_index -= 3

  return ''.join(chars)



if __name__ == '__main__':
  assert urlify(list('Mr John Smith    '), 13) == 'Mr%20John%20Smith'
  assert urlify(list('nospaces'), 8) == 'nospaces'
  assert urlify(list('Mr  Two Spaces      '), 14) == 'Mr%20%20Two%20Spaces'
  assert urlify(list('spaceAtTheEnd   '), 14) == 'spaceAtTheEnd%20'
  assert urlify(list(' spaceAtTheBegining  '), 19) == '%20spaceAtTheBegining'
