year = input()
year = int(year)

def is_year_leap(year):
    if year % 4:
        return False
    else:
        return True

result = is_year_leap(year)
print(f"год {year}: {result}")


