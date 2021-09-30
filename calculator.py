#calculator.py

def sum(m,n):
    while(n != 0):
        if(n > 0):
            m+=1
            n-=1
        else:
            n+=1
    return m

def divide(m,n):
    if(n==0):
        return "Error: Division by 0 not possible"
    else:
        i = 0
        while(m != 0):
            if(n > 0):
                m-=n
                i+=1
            else:
                m+=n
                i-=1
            
    return i
"""
a = sum(4,-2)
b = divide(6,-3)

print(a)
print(b)
"""