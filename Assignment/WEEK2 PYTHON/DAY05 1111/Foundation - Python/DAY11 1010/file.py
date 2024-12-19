# File Handling - Handling and Manipulating the files
# human readble form or non-human readable form.
# Text files and Binary Files
# File needs to be available
# Open the file - open() - w, r, r+, a, x, rw
# Read the file - read(), readline(), readlines()
# Write in the File - write(), writelines()
# Apped the file
# close the file (Important activity to perform) - close()

# Open the file
file = open('test.txt', 'w')
# file = open('test.txt', 'r')
# file = open('test.txt', 'r+w')

# Write date to the file
file.write("Hey World!")
file.write("Welcome to hexaware Session!!")

# close the file
file.close()





file = open('test.txt', 'r')
file_content = file.read()
print(file_content)
file.close()
 
file = open('test.txt', 'a')
file.write("\nI have appended this line")
file.close()


# with Context Manager - with statement - this auto closes the file
with open('test.txt', 'r') as file:
    file_content = file.read()
    print(file_content)


# Binary files
# modes while opening - 'rb', 'wb', 'ab'
# audio, image, video, bin

file = open('test.bin', 'wb') # when I use 'w' mode, if file is unavailable, it will create the file
file.write(b'\x00\x01\x02\x03\x04')
file.close()

with open('test.bin', 'rb') as file:
    bin_data = file.read()
    print(bin_data)



with open('test.png', 'rb') as file:
    bin_data = file.read()
    # print(bin_data)

with open('test_copy.png', 'wb') as file:
    file.write(bin_data)