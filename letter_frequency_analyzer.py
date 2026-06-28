string = "I guess the only time most people think about in justice is when it happens to them."

string = list(string)

letters = {}

for i in range(len(string)):
    if string[i] not in letters:
        letters[string[i]] = 1
    else:
        letters[string[i]] += 1

while True:
    for i, j in letters.items():
        x = min(letters)
        if i == x:
            print(x, end=": ")
            print(j)
            break
    letters.pop(min(letters))
    if len(letters) == 0:
        break
