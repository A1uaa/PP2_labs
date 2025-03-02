import os

path = input("Enter file path: ")
if os.path.exists(path) and os.access(path, os.W_OK):
    os.remove(path)
    print("File deleted.")
else:
    print("File doesnt exist or access is denied.")
