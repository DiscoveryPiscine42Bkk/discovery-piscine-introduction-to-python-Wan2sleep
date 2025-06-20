import sys

if len(sys.argv) != 2:
    input_string = input("Please enter a string to check for 'z': ")
else:
    input_string = sys.argv[1]

z_count = input_string.count('z')

if z_count > 0:
    print('z' * z_count)
else:
    print("none")