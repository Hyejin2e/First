n = int(input())

for i in range(0,n):
    a,b = map(int, input().split())
    sum = a+b
    print('Case #{0}: {1}'.format(i+1, sum))
    