while True:
    num = int(input("Enter a number (or -1 to exit): "))
    if num == -1:
        break
    elif num % 2 == 0:
        print("Even")
    else:
        print("Odd")
