# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы 
# выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

with open ('a.txt','r') as n:
    list = n.read()
    print(list)
    list = list.split()
    for i in range(2, len(list)):
        if int(list[i])-1 == int(list[i-1]):
            continue
        else:
            print(int(list[i])-1)
