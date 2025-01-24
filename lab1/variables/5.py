#1
x = "fun"

def myfunc():
  print("Coding is " + x)

myfunc()

#2
x = "fun"

def myfunc():
  x = "interesting"
  print("Coding is " + x)

myfunc()

print("Coding is " + x)

#3
def myfunc():
  global x
  x = "interesting"

myfunc()

print("Coding is " + x)
