with open("lab6\\directories and files\\8src.txt") as src, open("lab6\\directories and files\\8dest.txt", "w") as dest:
    for line in src:
        dest.write(line)
