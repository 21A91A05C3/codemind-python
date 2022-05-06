string = input()

# find sum of digits
sum_digit = 0
for x in string:
    if x.isdigit():
        sum_digit += int(x)

# display result
print(sum_digit)