def histogram(lst):
    for num in lst:
        print('*' * num)

lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
histogram(lst)
