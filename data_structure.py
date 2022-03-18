from pprint import pprint
sentence = "This is a common interview question"

char_freq = {}

for letter in sentence:
    if not letter in char_freq:
        char_freq[letter] = 1
    else:
        char_freq[letter] += 1

pprint(char_freq,width=1)

char_freq_sorted = sorted(
    char_freq.items(),
    key=lambda kv:kv[1],
    reverse=True
    )

print(char_freq_sorted[:3])