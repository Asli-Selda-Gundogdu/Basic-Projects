#zodiac sign calculator
month = int(input("Your birth month (1-12): "))
day = int(input("Your birth day (1-31): "))
year = int(input("Your birth year (>=0): "))

if (month == 3 and 21<= day <= 31) or (month == 4 and 1 <= day <= 19):
    print(f"{day}/{month}/{year} → You are an Aries ♈.")
elif (month == 4 and 20<= day <=30) or (month == 5 and 1 <= day <= 20):
    print(f"{day}/{month}/{year} → You are a Taurus ♉.")
elif (month == 5 and 21 <= day <=31) or (month == 6 and 1<= day <= 20):
    print(f"{day}/{month}/{year} → You are a Gemini ♊.")
elif (month == 6 and 21 <= day <= 30) or (month == 7 and 1<= day <= 22):
    print(f"{day}/{month}/{year} → You are a Cancer ♋.")
elif (month == 7 and 23 <= day <= 31) or (month == 8 and 1 <= day <= 22):
    print(f"{day}/{month}/{year} → You are a Leo ♌.")
elif (month == 8 and 23 <= day <= 31) or (month == 9 and 1 <= day <= 22):
    print(f"{day}/{month}/{year} → You are a Virgo ♍.")
elif (month == 9 and 23 <= day <= 30) or (month == 10 and 1 <= day <=22):
    print(f"{day}/{month}/{year} → You are a Libra ♎.")
elif (month == 10 and 23 <= day <= 31) or (month == 11 and 1 <= day <= 21):
    print(f"{day}/{month}/{year} → You are a Scorpio ♏.")
elif (month == 11 and 22 <= day <= 30) or (month == 12 and 1 <= day <= 21):
    print(f"{day}/{month}/{year} → You are a Sagittarius ♐.")
elif (month == 12 and 22 <= day <= 31) or (month == 1 and 1<= day <= 19):
    print(f"{day}/{month}/{year} → You are a Capricorn ♑.")    
elif (month == 1 and 20 <= day <= 31) or (month == 2 and 1 <= day <= 18):
    print(f"{day}/{month}/{year} → You are an Aquarius ♒.")  
elif (month == 2 and 19 <= day <= 29) or (month == 3 and 1 <= day <= 20):
    #leap year calculation  
    if month == 2:
        if (year % 4 == 0 and 19 <= day <= 29) or (year % 4 != 0 and 19 <= day <= 28):
            print(f"{day}/{month}/{year} → You are a Pisces ♓.")
        else:
            print("Enter valid date!")    
    else:
        print(f"{day}/{month}/{year} → You are a Pisces ♓.")       
else:
    print("Enter a valid date!")    
