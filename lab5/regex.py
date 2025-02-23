import re

with open(r"C:\Users\Алуа\Desktop\PP2\lab5\regex_data.txt", "r", encoding="utf-8") as f:
    data = f.read()

print("Task 1")
matches = re.findall("a.*?b", data)
print(matches)

print("Task 2")
matches = re.findall("ab{2,3}", data)
print(matches)

print("Task 3")
matches = re.findall(r"\b[a-z]+_[a-z]+\b", data) 
print(matches)


print("Task 4")
matches = re.findall(r"[A-Z][a-z]+", data)
print(matches)

print("Task 5")
matches = re.findall(r"a+.b", data)
print(matches)

print("Task 6")
matches = re.sub(r"[.,]\s*", ":", data) 
print(matches)

print("Task 7")
matches = re.sub(r"_", '', data)
print(matches)

print("Task 8")
matches = re.findall(r"[A-Z][a-z]*", data)
print(matches)


print("Task 9")
matches = re.sub(r"([a-z])([A-Z])", r"\1 \2", data)
print(matches)

print("Task 10")
matches = re.sub(r"([a-z])([A-Z])", r"\1_\2", data).lower()
print(matches)