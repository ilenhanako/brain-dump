# Error: Did not use list method
number_of_days = 0
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        number_of_days = 31
        return number_of_days
    elif month == 4 or month == 6 or month == 9 or month == 11:
        number_of_days = 30
        return number_of_days
    elif is_leap(year) and month == 2:
        number_of_days = 28
        return number_of_days

  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)







