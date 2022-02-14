file = open("my_file.txt")
print(file)
contents = file.read()
print(contents)
file.close()


# the with keyword keeps us from having to manually close files 

with open("my_file.txt", mode="w") as file:
    contents = file.read()
    print(contents)
    file.write("New text.")