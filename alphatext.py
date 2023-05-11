def alphabet_position_from_file(filename):
    result = ""
    with open(filename, "r") as file:
        for line in file:
            for char in line:
                if char.isalpha():
                    position = ord(char.lower()) - 96
                    result += str(position) + " "
    return result[:-1]

# example usage
filename = "test.txt"
print(alphabet_position_from_file(filename))
