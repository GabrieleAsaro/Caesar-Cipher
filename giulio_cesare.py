text = input("Insert your text: ")

char_list = []

def printing(old_char, new_char):
    print('     ┌────┐')
    print(f'{old_char} -> │>>>3│ -> {new_char}')
    print('     └────┘')

def encipher(string):
    if string.isalpha():
        for char in string:
            calculation = (ord(char) - 97 + 3) % 26
            char_list.append(chr(calculation + 97))
            printing(char, chr(calculation + 97))
    else:
        print('This is not a valid char')

    result = ''
    for var in char_list:
        result = result + var
    
    print(f'Encrypted text: {result}')

encipher(text)