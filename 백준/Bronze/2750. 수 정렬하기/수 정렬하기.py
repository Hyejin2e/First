data_num = int(input())
lst = []
max = 0
for i in range(data_num):
    a = int(input())
    lst.append(a)
    
lst.sort()

for i in range(data_num):
  print(lst[i])