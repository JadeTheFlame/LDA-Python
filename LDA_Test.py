import nltk
nltk.download('brown')
nltk.download('gutenberg')
nltk.download('words')
from nltk import FreqDist
from nltk.corpus import brown
from nltk.corpus import gutenberg
from nltk.corpus import words

import os
if os.path.exists("words.txt"):
    os.remove("words.txt")
f = open("words.txt", "a")
for fi in words.words():
    f.write(fi) # print(fi)
    f.write(' \n')
f.close()

# frequency_list = FreqDist(i.lower() for i in brown.words())
# for fi in frequency_list.most_common()[:1000]:
#     print(fi[0])
# print(frequency_list.most_common()[:100])

# frequency_list = FreqDist(i.lower() for i in gutenberg.words())
# print(frequency_list.most_common()[:100])