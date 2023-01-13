n = int(input())

def piv(n):
  if n == 1 : return 1
  elif n == 0 : return 0
  else: return piv(n-1)+piv(n-2)

print(piv(n))