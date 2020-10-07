lst=[1,2,3,3,3,3,4,5]

def uniq_lst(ll):
    new_lst=[]
    for i in ll:
        if i in new_lst:
            pass
        else:
            new_lst.append(i)
    print (new_lst)

uniq_lst(lst)