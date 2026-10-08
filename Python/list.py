# List - It is mutable
marks = [98, 54, 95, 48, 10]
print(marks)

# List operation
# Length
print(len(marks))

# Index
print(marks[0])
print(marks[-1])

# Slicing
print(marks[0:3]) #Last index excluded
print(marks[-3:-1]) #[95, 48]
print(marks[-3:]) #[95, 48, 10]

# Loop
for score in marks:
    print(score) #Print all the element of marks one by one

# Append 
marks.append(50)
print(marks) #[98, 54, 95, 48, 10, 50]

# Insert
marks.insert(1, 30)
print(marks) #[98, 30, 54, 95, 48, 10, 50]

# Value exist or not
print(97 in marks) #False
print(98 in marks) #True

# Clear List
marks.clear()
print(marks) #[]
