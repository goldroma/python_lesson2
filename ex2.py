st1 = [1, 2, 3, 4, 5]
st2 = [5, 4, 3, 2, 1]
if len(st1) != len(st2):
        print("string is not equel")
else:
    mmax = len(st1)
    k = []
    for i in range(0, mmax):
        if st1[i] > st2[i]:
            k.append((st1[i]))
        else:
            k.append((st2[i]))
print(k)
