def fun1(n):
    return n*(n+1)/2


print("product of numbers  is ",fun1(4))

def fun2(n):
    product=0
    for i in range(1,n+1):
        product*=i
    return product
    
print("productof the number is ",fun2(4))


