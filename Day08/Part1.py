from collections import defaultdict as dd

file = [line.strip() for line in open("input.txt")]

digit_chars = dict()

digit_parts = 7

a = 'a'
b = 'b'
c = 'c'
d = 'd'
e = 'e'
f = 'f'
g = 'g'

digit_chars[0] = [a, b, c, e, f, g]
digit_chars[1] = [c, f]
digit_chars[2] = [a, c, d, e, g]
digit_chars[3] = [a, c, d, f, g]
digit_chars[4] = [b, c, d, f]
digit_chars[5] = [a, b, d, f, g]
digit_chars[6] = [a, b, d, e, f, g]
digit_chars[7] = [a, c, f]
digit_chars[8] = [a, b, c, d, e, f, g]
digit_chars[9] = [a, b, c, d, f, g]


for digit in digit_chars:
    digit_chars[digit].sort()

total = 0

wordDigits = {''.join(digit_chars[a]): a for a in digit_chars}
wordList = list(wordDigits)

letterA = ord('a')


def sort_word(w):
    sorted_word = list(w)
    sorted_word.sort()
    return ''.join(sorted_word)


def add_potential_mappings(potentials, word, digits, length, digit):
    if len(word) == length:
        for letter in word:
            for ds in digits[digit]:
                potentials[letter].add(ds)


def convert_word_with_current_mappings(mappings, word):
    converted_word = ''
    for t in range(0, len(word)):
        converted_word += mappings[ord(word[t]) - letterA]
    return converted_word


def go(mappings, all_potentials, line_words):
    global total
    if len(mappings) < digit_parts:

        letter_potentials = all_potentials[chr(letterA + len(mappings))]
        if len(letter_potentials) == 0:
            letter_potentials = digit_chars[8]

        for pot in letter_potentials:
            if pot in mappings:
                continue
            go(mappings + pot, all_potentials, line_words)
        return

    converted_words = []
    for line_word in line_words:
        converted_words.append(convert_word_with_current_mappings(mappings, line_word))

    for converted_word in converted_words:
        sorted_new_word = sort_word(converted_word)

        if sorted_new_word not in wordList:
            return

    for converted_word in converted_words[-4:]:
        if wordDigits[sort_word(converted_word)] in [1, 4, 7, 8]:
            total += 1


for line in file:
    sp = [[b for b in a.split(' ')] for a in line.split(' | ')]

    line_words = []
    for a in sp[0]:
        line_words.append(sort_word(a))
    for a in sp[1]:
        line_words.append(sort_word(a))

    potentialMappings = dd(lambda: set())

    for word in line_words:
        add_potential_mappings(potentialMappings, word, digit_chars, 3, 7)
        add_potential_mappings(potentialMappings, word, digit_chars, 2, 1)
        add_potential_mappings(potentialMappings, word, digit_chars, 4, 4)

    go("", potentialMappings, line_words)

print(total)
