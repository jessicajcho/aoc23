import re 

def isValid(r, g, b, valid_r, valid_g, valid_b):
  if (r <= valid_r and g <= valid_g and b <= valid_b):
    return True
  return False

def soln():
  sum = 0
  file = open('input/day2.txt', 'r')
  lines = file.readlines()
  for line in lines:
    tok_lst = re.split('; |:', line)
    isValidGame = True
    curGame = int(tok_lst[0].split(" ")[1])
    for token in tok_lst:
      print(token)
      r = 0
      g = 0
      b = 0
      red = re.search("\d red", token)
      if (red):
        r = int(red.group()[0])
      green = re.search("\d green", token)
      if (green):
        g = int(green.group()[0])
      blue = re.search("\d blue", token)
      if (blue): 
        b = int(blue.group()[0])

      if (not isValid(r, g, b, 12, 13, 14)):
        isValidGame = False
    if (isValidGame):
      sum += curGame

  return sum 

x = soln()
print(x)