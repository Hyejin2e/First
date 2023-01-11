n, k = map(int, input().split())
lst = []


a = list(map(int, input().split()))
lst.append(a)

lst = lst[0]
lst.sort(reverse = True)

print(lst[k-1])