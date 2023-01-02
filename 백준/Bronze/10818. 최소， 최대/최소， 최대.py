n = int(input())

n_list = list(map(int, input().split()))

min = n_list[0]
max = n_list[0]

for i in n_list:
    if i < min:
        min = i
    else:
        min = min
        
for j in n_list:
    if j > max:
        max = j
    else:
        max = max
        
print(min, max)