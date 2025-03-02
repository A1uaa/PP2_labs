import time
import math

num = int(input())
sec = int(input())

time.sleep(sec / 1000) 
result = math.sqrt(num)

print(f"Square root of {num} after {sec} milliseconds is {result}")
