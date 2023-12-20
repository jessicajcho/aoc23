import re, sys

def check_valid(r, g, b, valid_r, valid_g, valid_b):
  if (r <= valid_r and g <= valid_g and b <= valid_b):
    return True
  else:
    return False

def get_num_cubes(token, color):
  x = re.search("\d+ " + color, token)
  if (x):
    res = int(x.group().split(" ")[0])
  else:
    res = 0
  return res

def soln(lines):
  sum_valid_ids = 0
  sum_powers = 0
  for line in lines:
    token_lst = re.split('; |:', line)
    is_valid_game = True
    cur_game_id = int(token_lst[0].split(" ")[1])

    r_max = 0
    g_max = 0
    b_max = 0

    for i in range(1, len(token_lst)):
      token = token_lst[i]
      r = get_num_cubes(token, "red")
      g = get_num_cubes(token, "green")
      b = get_num_cubes(token, "blue")

      # update min vals
      r_max = max(r_max, r) 
      g_max = max(g_max, g) 
      b_max = max(b_max, b) 

      if (not check_valid(r, g, b, 12, 13, 14)):
        is_valid_game = False
    
    # calculate power and append
    sum_powers += (r_max * g_max * b_max)
    
    if (is_valid_game):
      sum_valid_ids += cur_game_id

  return sum_valid_ids, sum_powers

file = open('input/day2.txt', 'r')
lines = file.readlines()
x = soln(lines)
# tuple (part a, part b)
print(x)