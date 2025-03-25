new_alphabet_dic = {
    "a": "@",
    "b": "8",
    "c": "(",
    "d": "|)",
    "e": "3",
    "f": "#",
    "g": "6",
    "h": "[-]",
    "i": "|",
    "j": "_|",
    "k": "|<",
    "l": "1",
    "m": "[]\\/[]",
    "n": "[]\\[]",
    "o": "0",
    "p": "|D",
    "q": "(,)",
    "r": "|Z",
    "s": "$",
    "t": "']['",
    "u": "|_|",
    "v": "\\/",
    "w": "\\/\\/",
    "x": "}{",
    "y": "`/",
    "z": "2",
}

input_string = input().lower()
new_alphabet = ""

for c in input_string:
    if c in new_alphabet_dic:
        new_alphabet += new_alphabet_dic[c]
        continue
    new_alphabet += c
    
print(new_alphabet)