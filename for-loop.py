
friends = ["Kevin", "Jim", "Oscar"]

# loop in string
for letter in "Some string":
    # print(letter)

# loop in list
for friend in friends:
    print(friend)

# range, last number is excluded
for i in range(0, 10):
    print(i)

def raise_to_power(base_number, power_number) -> int:
    result = 1
    for idx in range(power_number):
        result *= base_number
    return result

print(raise_to_power(2, 2))