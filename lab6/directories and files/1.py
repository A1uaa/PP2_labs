import os

def list_items(path):
    try:
        items = os.listdir(path)
        print("Directories:", [d for d in items if os.path.isdir(os.path.join(path, d))])
        print("Files:", [f for f in items if os.path.isfile(os.path.join(path, f))])
        print("All Items:", items)
    except FileNotFoundError:
        print("Invalid path!")

path = input("Enter the directory path: ")
list_items(path)
#C:\Users\Алуа\Desktop\PP2\lab5