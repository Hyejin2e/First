import sys

n = int(sys.stdin.readline().rstrip())
lst = []
sum = 0

for i in range(n):
  a = int(sys.stdin.readline().rstrip())
  
  
  if a == 0 : lst.pop(-1)
  else: lst.append(a)

for i in range(len(lst)):
  sum += lst[i]

print(sum)