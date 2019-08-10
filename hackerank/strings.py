if __name__ == '__main__':
    string = input()
    isalnum = False
    isalpha = False
    isdigit = False
    islower = False
    isupper = False
    for letter in string:
        if letter.isalnum():
            isalnum = True
        if letter.isalpha():
            isalpha = True
        if letter.isdigit():
            isdigit = True
        if letter.islower():
            islower = True
        if letter.isupper():
            isupper = True


    print(isalnum)
    print(isalpha)
    print(isdigit)
    print(islower)
    print(isupper)