def clocky(hour, minute, period):
    # calculating 
    hour = (hour % 12 + (period.lower() == 'pm') * 12) % 24

    # the appearance of output
    result = "{:02d}{:02d}".format(hour, minute)
    return result


print(clocky(8, 30, 'am'))  # printing of output
print(clocky(11, 45, 'pm'))  # printing of output
print(clocky(1, 37, 'am'))  # printing of output
print(clocky(12, 12, 'pm')) # printing of output