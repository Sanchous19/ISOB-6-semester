import sys


alphabet_len = 26
first_letter = ord('A')


def helper(func):
    def wrapper(char, key):
        if char.isalpha():
            shift = ord(char.upper()) - first_letter
            return func(char, key, shift)
        else:
            return char
    return wrapper


@helper
def encrypt(char, key, shift):
    return chr((ord(char) - shift) + (shift + key) % alphabet_len)


@helper
def decrypt(char, key, shift):
    return chr((ord(char) - shift) + (shift - key) % alphabet_len)


def main():
    file_name, key, mode = sys.argv[1:4]
    key = int(key)
    solve_fun = encrypt if mode == 'e' else decrypt
    with open(file_name, 'r') as f:
        for line in f:
            line = line.rstrip()
            line = ''.join(map(lambda char: solve_fun(char, key), line))
            print(line)


if __name__ == '__main__':
    main()
