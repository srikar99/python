

# reading file

"""
we can open file in 4 modes

1: Read
To open file in read mode use open(filename, "r")

2: Write
To open file in write mode use open(filename, "w")

3: Append
To open file in read mode use open(filename, "a")

4: Read/Write
To open file in read mode use open(filename, "r+")

"""
emp_file = open("emp.txt", "r")

# read a single line
print(emp_file.readline())

# read all lines
for emp in emp_file.readlines():
    print(emp)

# read all lines puts each line in a list
# example
# it won't print anything now, as the cursor is already at EOF from the for loop
# to print all lines, comment out the above code
print(emp_file.readlines())

emp_file.close()
