def solution(quiz):
    lst = []
    for i in range(len(quiz)):
      a  = quiz[i].split()
      if a[1] == '-':
        b = int(a[0]) - int(a[2]) 
        if str(b) == a[-1]:
          answer = 'O'
        else:
          answer = 'X'
        lst.append(answer)

      else:
        b = int(a[0]) + int(a[2]) 
        if str(b) == a[-1]:
          answer = 'O'
        else:
          answer = 'X'
        lst.append(answer)
    return lst