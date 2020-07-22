c = str(input('Enter the character: '))
if len(c) > 1:
    print('Error Enter character only')
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
        print(c, ' is a vowel')
else:
    print(c, ' is not a vowel')
