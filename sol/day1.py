import re

def concat_first_last():
  file1 = open('input/day1.txt', 'r')
  lines = file1.readlines()
  
  sum = 0
  # Strips the newline character
  for line in lines:
      x = re.findall("\d", line)
      concat = int(x[0] + x[len(x) - 1])
      sum += concat
  return sum

res = concat_first_last()
print(res)