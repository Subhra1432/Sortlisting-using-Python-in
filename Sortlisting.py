# Returns the length of a given string
def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

# Sorts a list of strings by their lengths
def sort_by_length(strings):
    n = len(strings)
    n = 0
    for _ in strings:
        n += 1
    for i in range(n):
        for j in range(0, n - i - 1):
            if string_length(strings[j]) > string_length(strings[j + 1]):
                # Swap strings[j] and strings[j + 1]
                strings[j], strings[j + 1] = strings[j + 1], strings[j]
    return strings

# Get the number of strings to sort from the user
n = int(input("Enter the number of strings: "))
strings = [None] * n
for i in range(n):
    strings[i] = input(f"Enter string {i + 1}: ")

# Sort the strings by length
sorted_strings = sort_by_length(strings)
print("Sorted list based on string lengths:", sorted_strings)