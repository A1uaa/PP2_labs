from datetime import datetime

date1 = input("Enter first date (YYYY-MM-DD HH:MM:SS): ").strip()
date2 = input("Enter second date (YYYY-MM-DD HH:MM:SS): ").strip()

format = "%Y-%m-%d %H:%M:%S"
datetime1 = datetime.strptime(date1, format)
datetime2 = datetime.strptime(date2, format)
difference = abs(datetime2 - datetime1)
difference_in_seconds = difference.total_seconds()

print("The difference in seconds is:", difference_in_seconds)
