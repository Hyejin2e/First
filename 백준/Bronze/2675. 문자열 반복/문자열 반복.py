r = int(input())
ans = ''


for i in range(r):
    a, b = input().split()
    for j in range(len(b)):
      for k in range(int(a)):
        ans += (b[j])
    print(ans)
    ans = ''
                  
         
         