

# try with general except

try:
    num = int(input("Enter number for general except: "))
    print(num)
except:
    print("Not a number")

# specific except

try:
    num = int(input("Enter number for specific except: "))
    print(num)
except ValueError:
    print("Value error")


# Multi except

try:
    num = int(input("Enter number for multi except: "))
    num / 0
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
