# x=int(input("enter the no"))
# def n(a):
#     print(a)
#     if (a==0):
#      return
#     else:
#        return n(a-1)


# n(x)


def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)           

n=input("Enter a number: ")
print("Sum of first", n, "natural numbers is:", sum(int(n)))    
    