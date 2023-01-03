n_list = []
a_list = list(range(1,31))

for i in range(1,29):
    a = int(input())
    n_list.append(a)

minus = set(a_list)-set(n_list)
        
print(min(minus))
print(max(minus))