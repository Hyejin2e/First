data = str(input())

a_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ans = ''


for i in range(len(a_list)):
    if a_list[i] in data:
        p_data = str(data.index(a_list[i]))
    else:
        p_data = str('-1')
    ans += (p_data + ' ')
print(ans)