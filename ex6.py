def find_min():
    data=[]
    # min=0
    for i in range(0,5):
        a = int(input("enter the number:"))
        data.append(a)
    print (data)
    min=data[0]
    for i in data:
        if min>i:
            min = i
    print('the min in list is  :', min)

find_min()