import nltk
nltk.download('wordnet')

from nltk.corpus import wordnet

from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

# Lemmatize example
verbs = ['went', 'flew', 'ran', 'swimming', 'jumped', 'lm', 'gyroscoped']

tagged = nltk.pos_tag(verbs)

pos_list = ['a','s','r','n','v']
for word, tag in tagged:
    for posi in pos_list:
            lemma = lemmatizer.lemmatize(word, pos=posi)
            if lemma is not word:
                break
    print(lemma)
