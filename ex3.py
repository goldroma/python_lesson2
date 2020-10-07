# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list1 = [1, 2, 3, 'str11', 5, 6, 7, 8, 9]

even = 0
odd = 0
for i in list1:
    if isinstance(i,str) is True:
        print('It’s a string!!!')
        exit(0)
    else:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

print ('Number of even numbers : '+str(even))
print ('Number of odd numbers : '+str(odd))