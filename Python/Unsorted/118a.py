vowels = [i for i in "aeiouyAEIOUY"]
string_in = [i for i in input() if i not in vowels]
string_in.insert(0,"")
print(".".join(string_in).lower())
