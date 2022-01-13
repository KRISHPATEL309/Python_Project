# Q-4
# Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
Disk1 = {
    0:10,
    1:20,
}
print("Sample Dictionary : ")
print(Disk1)
print("Add a key to a dictionary :")
((Disk1.update({2 : 30}))) #updates the dictionary by adding key-value pair.
print(Disk1)