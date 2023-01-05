data = str(input())

cnt = data.count(' ')

cnt += 1

if (data[0] == ' ') :
  cnt -= 1
if (data[-1] == ' '):
  cnt -=1
print(cnt)