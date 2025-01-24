#1
price = 59
item= "apple"
txt = f"The item {item} price is {price} dollars"
print(txt)

#2
price = 59
item= "apple"
myorder = "The item {} price is {} dollars"
print(myorder.format(item, price))