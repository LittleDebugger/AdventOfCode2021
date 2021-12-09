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

digit_chars[0] = [c, a, g, e, d, b]
digit_chars[1] = [a, b]
digit_chars[2] = [g, c, d, f, a]
digit_chars[3] = [f, b, c, a, d]
digit_chars[4] = [e, a, f, b]
digit_chars[5] = [c, d, f, b, e]
digit_chars[6] = [c, d, f, g, e, b]
digit_chars[7] = [d, a, b]
digit_chars[8] = [a, c, e, d, g, f, b]
digit_chars[9] = [c, e, f, a, b, d]

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
    good_word = ''
    for t in range(0, len(word)):
        good_word += mappings[ord(word[t]) - letterA]
    return good_word


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

    output_num = ''
    for converted_word in converted_words[-4:]:
        output_num += str(wordDigits[sort_word(converted_word)])

    total += int(output_num)


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
