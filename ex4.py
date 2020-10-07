ll =[1,2,3,4,'aa']

def sum_list(aa):
    sum = 0
    for i in aa :
        if isinstance(i,str) is True:
            print('It’s a string!!!')
            exit(0)
        else:
            sum = sum + i
    return sum

print(sum_list(ll))
