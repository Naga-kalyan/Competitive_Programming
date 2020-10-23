if __name__ == '__main__':
    s = input()
    print(any(letter.isalnum() for letter in s))
    print(any(letter.isalpha() for letter in s))
    print(any(letter.isdigit() for letter in s))
    print(any(letter.islower() for letter in s))
    print(any(letter.isupper() for letter in s))
