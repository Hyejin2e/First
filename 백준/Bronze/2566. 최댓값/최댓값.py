lst = []
max = 0
max_row = 0
max_col = 0
for i in range(9):
  lst_row = list(map(int, input().split()))
  lst.append(lst_row)

for i in range(9):
  for j in range(9):
    if lst[i][j] > max:
      max = lst[i][j]
      max_row = i
      max_col = j
    else:
      max = max
      max_row = max_row
      max_col = max_col



print(max)
print(max_row+1,max_col+1)