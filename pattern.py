# Make number of lines equal to 5
num_of_lines = 5

# for loop containing if-else statement to output the pattern
for i in range(1, 2 * num_of_lines):
    if i <= num_of_lines:
        print('*' * i)
    else:
        print('*' * (2 * num_of_lines - i))
