import hashlib

print("This is an example of how HASHing works using md5.")

print("Please enter three string values of different lengths:\n")

myDictionary = {}

for i in range(3):
    myString = input("Enter a string value to hash: ")
    hash_object = hashlib.md5(myString.encode())
    hash_value = hash_object.hexdigest()

    myDictionary[myString] = hash_value

for key in myDictionary:
    print("{0} is hashed into value: \t{1}".format(key, myDictionary[key]))

print("\nHashing will format whatever string size into the same length.\n")


print("\nThe problem with some hashing standards such as md5 is as follows:\n")
print("This time enter 'password' to be hashed...\n")

myString = input("Enter a string value to hash: ")
hash_object = hashlib.md5(myString.encode())
hash_value = hash_object.hexdigest()

print("{0} is hashed into value: \t{1}".format(myString, hash_value))
print("\nNow search for this HASH VALUE REVERSED in Google and see what you find!!\n")

