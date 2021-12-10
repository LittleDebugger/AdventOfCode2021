file = [line.strip() for line in open("input.txt")]

t = 0
totals = []

for line in file:
    stack = []
    good = True

    for c in line:
        if c in ['(', '{', '[', '<']:
            stack.append(c)
            continue

        if c in [')', '}', ']', '>']:

            top = stack.pop()
            if (top == '(' and c != ')') or \
                    (top == '[' and c != ']') or\
                    (top == '{' and c != '}') or\
                    (top == '<' and c != '>'):

                good = False
                break

    if good == False:
        continue

    if len(stack) > 0:
        t = 0
        stack.reverse()

        for c in stack:
            t = t * 5

            if c == '(':
                t += 1
            if c == '[':
                t += 2
            if c == '{':
                t += 3
            if c == '<':
                t += 4

        totals.append(t)

print(totals[(len(totals) // 2)])
