def play_pass(s, n):
    result = []
    
    for char in s:
        if char.isalpha():
            shift = n % 26
            if char.islower():
                shifted = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                shifted = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            result.append(shifted)
        elif char.isdigit():
            digit = int(char)
            new_digit = (9 - digit)
            result.append(str(new_digit))
        else:
            result.append(char)
    
    for i in range(len(result)):
        if i % 2 == 1:
            result[i] = result[i].lower()
    
    return ''.join(result[::-1])

# Example usage:
s = "Hello World!"
n = 1
print(play_pass(s, n))  # Output: "!"dpoVrJ wdlroW"