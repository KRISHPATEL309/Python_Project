# Q-3
# Write a Python program to sum all the items in a dictionary.
Disk = {
    "Marks1" : 10,
    "Marks2" : 20,
    "Marks3" : 50
}
sum = 0
for i in Disk.values() :
    sum = sum +i

print("Sum of values : ",sum)