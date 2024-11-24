
word = input()
vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
letters = len(word)
num_vowels = 0
for vowel in word:
    if vowel in vowels:
        num_vowels += 1
consonants = letters - num_vowels
print(f" В слове[{word}] {letters} букв, гласных - {num_vowels} и согласных - {consonants}.")

for vowel in vowels:
    count=word.count(vowel)
    if count==0:
        print(f" гласной {vowel}: False")
    else:
        print(f" гласной {vowel}: {count}")
