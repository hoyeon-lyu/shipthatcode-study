year = int(input())

# One boolean expression over `year` goes here. It must be True for exactly
# the leap years. Replace False; do not change the printing below.

# from website: 
# The rule: a year is a leap year if it is divisible by 4, 
# EXCEPT years divisible by 100, which are not,
# UNLESS they are also divisible by 400, which are.

is_leap = year % 4 == 0 and not year % 100 == 0 or year % 400 == 0

if is_leap:
    print("leap")
else:
    print("not leap")
