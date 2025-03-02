import os
import string

folder = r"C:\Users\Алуа\Desktop\PP2\lab6\directories and files"
os.makedirs(folder, exist_ok=True)

for letter in string.ascii_uppercase:
    with open(os.path.join(folder, letter + ".txt"), "w") as file:
        file.write("This is " + letter + ".txt file.")
