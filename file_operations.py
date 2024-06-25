# opening a file
# file path relative to the running .py script
# call open function and pass the name of the file in quotes,
#     if the file is not in relative to itself then you have to pass in full path, so it can be found


# opens file in same directory as running pyfile
# file = open("test.txt")

# defaults to r "Read" and t "Text"
# file2 = open("test.txt", "rt")


# open("test.txt")
# w is for write, updating the text file
# open("test.txt", 'w')
# b for binary data, for images, etc.
# open("img.bmp", 'r+b')


# https://www.w3schools.com/python/python_file_handling.asp

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode(e.g. images)


# reading and closing
file3 = open("test.txt")

read_content = file3.read()
print(read_content)

file3.close()

# writing
file4 = open("test.txt", "w")

if file4.writable():
    file4.write("This is new text")

file4.close()

