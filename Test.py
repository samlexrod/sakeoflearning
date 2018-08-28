# string to read
cool_hand_luke = "What we've got here is... failure to communicate. Some men you just can't reach. So you get what we had here last week, which is the way he wants it... well, he gets it. I don't like it any more than you men."

# declaring the dictionary of letter counts
letter_count = {}

# constructing the dictionary of letter counts
for letter in cool_hand_luke.upper():
    # to handle incrementing errors
    letter_count.setdefault(letter, 0)

    # incrementing
    letter_count[letter] = letter_count[letter] + 1

from pprint import pprint, pformat
#pprint(letter_count)

print(type(pprint(letter_count)))


