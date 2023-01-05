a, b = map(str, input().split())
a1 = ''
b1 = ''

for i in range(3):
    a1 += a[len(a)-(len(a)+1+i)]
a1 = int(a1)

for j in range(3):
    b1 += b[len(b)-(len(b)+1+j)]
b1 = int(b1)

if a1 > b1 :
  print(a1)
else:
  print(b1)