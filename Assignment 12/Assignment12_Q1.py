def CheckCharacter(ch):
    if ch in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
        print("Vowel")
    else:
        print("Consonant")

char = input("Enter a character: ")
CheckCharacter(char)