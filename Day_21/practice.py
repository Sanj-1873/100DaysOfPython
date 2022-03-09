#FileNotFound
# with open("a_file.txt") as file:
#     fuile.read()

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    # print(a_dictionary["sadf"])
except FileNotFoundError:
    open("a_file.txt", "w")
    print("We did't find a_file.txt, creating one.")
except KeyError as error_message:
    print("The key {} does not exist" .format(error_message))
else: 
    content = file.read()
    print(content)
finally:
    file.close()
    print("file was closed")

# KeyError 
# a_dictionary = {"key":"value"}
# value = a_dictionary["non_existent_key"]

# type KeyError
# text = "abc"
# print(text + 5)