# Q-1
# Write a Python script to check whether a given key already exists in a dictionary.
def check(a):
    if a in Disk1:
         print("given key already exists in a dictionary.")
    else:
         print("given key not exists in a dictionary.")

Disk1 = {
    "key" : "Value",
    "krish" : "Name",
    "Marks" : "95",
    "List" : [95,100,43],
    "Anotherdict" : {"krish" : "coder"}
}
b = input("Enter any key name:")
check(b)