import hashlib

myString = input("Enter a string value to hash: ")

hash_object = hashlib.md5(myString.encode())

print("{0} is hashed into value: {1}".format(myString, hash_object.hexdigest))
