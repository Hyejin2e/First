lst = []
sum = 0
med = 0
for i in range(5):
  data = int(input())
  lst.append(data)

for i in range(5):
  sum += lst[i]

lst.sort()

med = lst[2]
avg = int(sum / 5)

print(avg)
print(med)