def pyramid(rows):
    for i in range(1, rows + 1):
        # Print spaces
        print(' ' * (rows - i), end='')
        # Print stars
        print('*' * (2 * i - 1))

def reverse_pyramid(rows):
    for i in range(rows, 0, -1):
        # Print spaces
        print(' ' * (rows - i), end='')
        # Print stars
        print('*' * (2 * i - 1))

# Take user input
n = int(input("Enter the number of rows: "))

print("\nPyramid:")
pyramid(n)

print("\nReverse Pyramid:")
reverse_pyramid(n)