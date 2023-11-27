def clocky(hour, minute, period):

    hour = (hour % 12 + (period.lower() == 'pm') * 12) % 24

  
    result = "{:02d}{:02d}".format(hour, minute)
    return result


print(clocky(8, 30, 'am'))
print(clocky(11, 45, 'pm'))  
print(clocky(1, 37, 'am')) 
print(clocky(12, 12, 'pm')) 