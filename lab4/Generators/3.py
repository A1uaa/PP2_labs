def d34(n):
    for i in range(n+1):
        if i%3 == 0 and i%4==0:
            yield i
            
n = int(input("n:"))
for num in d34(n):
    print(num)