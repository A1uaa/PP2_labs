from datetime import date, timedelta

current = date.today() - timedelta(days=5) 
print("Current date: ", date.today()) 
print("Subtract five days: ", current)  
