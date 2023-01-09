s = input().upper()
lst = [0] * 26
cnt = 0
a = 0
b = 0

for i in s:
    lst[ord(i) - 65] += 1

for i in range(len(lst)):
    if lst[i] > a :
        a = lst[i]
        b = i

for i in range(len(lst)):
    if a == lst[i]: cnt += 1

if cnt >= 2: print("?")
else: print(chr(b+65))