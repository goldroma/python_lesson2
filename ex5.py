# import sys
# data = []
# while True:
#     if input("enter the number:") == 'no':
#         print(data)
#         break
#     else:
#         data = data.append(input("enter the number:"))
#

# print(sys.version)
# data =input("enter the number:")
# print(data)
def create_list():
    data=[]
    for i in range(0,5):
        a = int(input("enter the number:"))
        data.append(a)
    print (data)

create_list()