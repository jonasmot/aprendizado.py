def is_leap(year):
    leap = False

    l = year % 4 == 0  # is True, unless:
    i = year % 100 == 0  # is False, unless
    p = year % 400 == 0  # is True

    # Write your logic here
    if (year > 1900 and year < 10 ** 5):
        if (l and i and p):
            leap = True
        else:
            if (l):
                if (not i):
                    leap = True
                if (i):
                    if (p):
                        leap = True

    return leap


year = int(input("Digite seu ano: "))
print(is_leap(year))