import sys

n = int(sys.stdin.readline().rstrip())

lst = []
ans_lst = []

for i in range(n):
  a = list(sys.stdin.readline().rstrip().split())
  lst.append(a)

  if len(a) == 2:
    mend = lst[i][0]
    num = lst[i][1]
  else: 
    mend = lst[i][0]

  if mend == 'push' : ans_lst.append(int(num))
  elif mend == 'pop' : 
    if len(ans_lst) == 0 : print('-1')
    else: 
      print(ans_lst[-1])
      ans_lst.pop(-1)
  elif mend =='size': print(len(ans_lst))
  elif mend == 'empty':
    if len(ans_lst) == 0:
      print('1')
    else:
      print('0')
  elif mend == 'top':
    if len(ans_lst) == 0 : print('-1')
    else: print(ans_lst[-1])


