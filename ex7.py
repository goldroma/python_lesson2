str1 = 'Alex Kuznetsov'
# print (len(str1))
def check_up_low_str(str11):
    uppercase = 0
    lowercase= 0
    for i in str1:
        if i.isupper():
            uppercase = uppercase+1
            # print(i)
        elif i.islower():
            lowercase = lowercase+1
        else:
            pass
    print ('No. of Upper case characters:'+str(uppercase))
    print('No. of Lower case characters:' + str(lowercase))
    # return(lowercase,uppercase)


check_up_low_str(str1)