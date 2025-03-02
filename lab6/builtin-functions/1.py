import functools

num = list(map(int, input("Enter numbers: ").split()))
res = functools.reduce(lambda x, y: x * y, num)
print("Product:", res)
