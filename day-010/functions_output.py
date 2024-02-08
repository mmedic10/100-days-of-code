# Functions with outputs

def format_name(f_name,l_name):
    """Take a first name and last name and format it to return the title case version of the name."""
    if f_name=="" or l_name =="":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return  f"Result: {formated_f_name} {formated_l_name}"


print(format_name(input("What's your first name"),input("What's your last name?")))

# El return termina la ejecucion del codigo

# Ejercicio: Days in month

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                #print("Leap year")
                return True
            else:
            #print("Not leap year")
                return False
        else:
        #print("Leap year")
            return True
    else:
    #print("Not leap year")
        return False

# TODO: Add more code here 👇
def days_in_month(year,month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    leap_year = is_leap(year)
    day = month_days[month-1]
    if leap_year == True and month==2:
        day+=1
        return day
    else:
        return day
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)
