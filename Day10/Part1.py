file = [line.strip() for line in open("input.txt")]

t = 0

for line in file:
    stack = []
    i = 0
    for c in line:
        if c in ['(', '{', '[', '<']:
            stack.append(c)
            continue

        if c in [')', '}', ']', '>']:
            if len(stack) == 0:
                break

            top = stack.pop()
            if (top == '(' and c != ')') or \
                    (top == '[' and c != ']') or\
                    (top == '{' and c != '}') or\
                    (top == '<' and c != '>'):
                if c == ')':
                    t += 3
                    break
                if c == ']':
                    t += 57
                    break
                if c == '}':
                    t += 1197
                    break
                if c == '>':
                    t += 25137
                    break

print(t)
