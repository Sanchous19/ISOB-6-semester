import sys

import сaesar as caesar


alphabet_len = 26
first_letter = ord('A')


def get_gen_key(key_word):
    while True:
        for let in key_word:
            yield ord(let.upper()) - first_letter


def main():
    file_name, key_word, mode = sys.argv[1:4]
    gen_key = get_gen_key(key_word)
    solve_fun = caesar.encrypt if mode == 'e' else caesar.decrypt
    with open(file_name, 'r') as f:
        for line in f:
            line = line.rstrip()
            line = ''.join(map(lambda char: solve_fun(char, next(gen_key)), line))
            print(line)


if __name__ == '__main__':
    main()
