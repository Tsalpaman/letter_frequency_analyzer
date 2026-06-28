string = """
How the hell could a person enjoy being awakened at 6:30AM, 
by an alarm clock, leap out of bed, dress, force-feed, shit, piss, 
brush teeth and hair, and fight traffic to get to a place 
where essentially you made lots of money for somebody else 
and were asked to be grateful for the opportunity to do so?"""

new_string = string.lower()
new_stringstring = list(new_string)

letters = {}

for i in range(len(string)):
    if new_string[i] not in letters:
        letters[new_string[i]] = 1
    else:
        letters[new_string[i]] += 1

while True:
    for i, j in letters.items():
        x = min(letters)
        if i == x and "a" <= i <= "z":
            print(x, end=": ")
            print(j)
            break
    letters.pop(min(letters))
    if len(letters) == 0:
        break
