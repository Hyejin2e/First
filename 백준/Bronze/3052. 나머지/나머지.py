li=[]
ans = []
for i in range(0,10):
    a = int(input())
    b = a % 42
    ans.append(b)
    
ans = set(ans)

print(len(ans))