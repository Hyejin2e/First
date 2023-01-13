import sys

n = int(sys.stdin.readline().rstrip())

lst = []
for i in range(n):
  a = int(sys.stdin.readline().rstrip())
  lst.append(a)
lst.sort()

for i in range(n):
  print(lst[i])