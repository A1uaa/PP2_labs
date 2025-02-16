def evens(n):
    for i in range(0,n+1,2):
        yield i

n=int(input("n:"))
print(",".join(map(str, evens(n))))