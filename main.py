# Line 1 of the input is a whole number, line 2 is a decimal number.
whole_text = input()
decimal_text = input()

# TODO: turn the two lines of text into numbers and add them up
whole_number = int(whole_text)
decimal_number = float(decimal_text)

summary = float(whole_number) + decimal_number


print(summary)   # the sum, as a decimal
print(int(summary))   # the same sum with the fraction chopped off toward zero
print(f"{whole_number} + {decimal_number} = {summary}")   # the report line
