
# if-else conditional statements

is_male = False
is_tall = False

if is_male and is_tall:
    print("You are male and tall")
elif is_male and not is_tall:
    print("You are male and short")
elif not is_male and is_tall:
    print("You are not male and tall")
elif not is_male and not is_tall:
    print("You're not male and not tall")
else:
    print("You are neither male nor tall")

# conditional statements continued


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


result = max_num(10, 4, 6)

print(result)

