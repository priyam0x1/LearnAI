# Dictionary => Collection of Key : Value Pairs
# It is mutable

marks = {
    "maths" : 97,
    "chemistry" : 78,
    "computer" : 67
}
print(marks)

# Accesing Through Key
print(marks["maths"]) # 97

# Add New Key
marks["English"] = 90 # {'maths': 97, 'chemistry': 78, 'computer': 67, 'English': 90}
print(marks)

# loop
for key in marks:
    print(key, marks[key])