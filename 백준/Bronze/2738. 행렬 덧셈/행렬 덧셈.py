rows, cols = map(int, input().split())

arr_a = []

arr_b = []

arr_sum = [[0 for i in range(cols)] for j in range(rows)]

for i in range(rows):
    lst_a = list(map(int, input().split()))
    arr_a.append(lst_a)

for i in range(rows):
    lst_b = list(map(int, input().split()))
    arr_b.append(lst_b)


for i in range(rows):
  for j in range(cols):
    arr_sum[i][j] = arr_a[i][j] + arr_b[i][j]

    if j != (cols-1):
      print(arr_sum[i][j], end = ' ')
    else:
      print(arr_sum[i][j])