case = int(input())

sum = 1

count = 1

for i in range(case):

    sum = 1

    count=1

    str1 = str(input())

    if str1[0]=='O':

      sum=1

      for j in range(len(str1)-1):

        if (str1[j+1] == 'O'):

          count += 1

        else:

          count=0       

        sum+=count

      print(sum)

    else:

      sum=0

      count=0

      for j in range(len(str1)-1):

        if (str1[j+1] == 'O'):

          count += 1

        else:

          count=0

        sum+=count

        

      print(sum)