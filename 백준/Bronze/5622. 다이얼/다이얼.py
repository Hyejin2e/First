
data = list(str(input()))
a3 = ['A','B','C']
a4 = ['D','E','F']
a5 = ['G','H','I']
a6 = ['J','K','L']
a7 = ['M','N','O']
a8 = ['P','Q','R','S']
a9 = ['T','U','V']
a10 =['W','X','Y','Z']

point = 0
point_sum = 0

for i in range(len(data)):
    if data[i] in a3:
        point = 3
    elif data[i] in a4:
        point = 4
    elif data[i] in a5:
        point = 5
    elif data[i] in a6:
        point = 6
    elif data[i] in a7:
        point = 7
    elif data[i] in a8:
        point = 8
    elif data[i] in a9:
        point = 9
    elif data[i] in a10:
        point = 10
    point_sum += point


print(point_sum)