
month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sept": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(month_conversions["Jan"])
print(month_conversions.get("Dec"))
print(month_conversions.get("December", "Not a valid key"))

# while loops

i = 1
while i <= 10:
    print(i)
    i += 1



