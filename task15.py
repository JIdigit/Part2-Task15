age=int(input())
check=age%2
i=0
while check==0:
    print(i)
    i+=2
    if i>age:
        break
else:
    print(list(range(1,age,2)))