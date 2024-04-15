f=1
n= int(input("Enter the factorial number: "))

def fact(f,n):
    for i in range(1,n+1):
        f=f*i
    return f

result = fact(f,n)

print(result)
