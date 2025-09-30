#date
month = int(input("Your birth month (1-12): "))
day = int(input("Your birth day (1-31): "))
year = int(input("Your birth year (>=0): "))
print(day ,"/" , month , "/" , year)

valid = False

if 1<= month <=12 and year>=0:
    if month in [1,3,5,7,8,10,12]:
        if 1<= day <=31:
            valid = True
    elif month == 2:
        if year % 4 == 0:
            if 1 <= day <= 29:
                valid = True
        else:
            if 1<= day <= 28:
                valid = False   
    else:
        if 0 <= day <= 30:
            valid = True

if valid:
    print("Valid date!")
else: 
    print("Invalid date!")    

        