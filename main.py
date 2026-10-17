code = input()
amount = int(input())

# Replace each placeholder below with the comparison described in the comment.
print(code == "GOLD")  # TODO: is the code exactly GOLD?
print("X" in code)  # TODO: does the code contain an X?
print(amount >= 50 and amount <= 200)  # TODO: is the amount between 50 and 200, both ends included?
print(code == "GOLD" or not (amount >= 50 and amount <= 200))  # TODO: exactly GOLD, or the amount outside that band?
