def square_numbers(N):
    for i in range(N + 1):
        yield i * i

N = int(input("Enter N: "))
for num in square_numbers(N):
    print(num)
