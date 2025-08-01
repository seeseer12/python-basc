# f=open("demo.txt","r")
# data=f.read()
# print(data)
# print(type(data))
# # f.seek(0)  -> after read func pointer is at last so seek for repoint at initial
# s=f.read(4)
# print(s)
# f.seek(0)
# print(f.readline())
# print(f.readline())
# f.close()


# r-  open for reading(default)
# w-  open for writting, truncating the file first
# =  open a disk file for updating (reading and writing)





# redaing in file
# f=open("demo.txt","r")
# for i in range (2):
#     print(f.readline().strip())
# f.close()

# strip for new line avoid






# writing in file
# f=open("iloveher.txt",'w')
# f.write("actually she is loyal too!!")
# # print(f.read())
# f.close()



# prpoer syntax or lets say opt
with open("demo.txt") as f:
    print(f.read())

with open("demo.txt","w") as shishir:
    shishir.write("haha no need of f.close function")