import os
import pandas as pd
import nltk
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import numpy as np
from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer
np.random.seed(999)
lemmatizer = WordNetLemmatizer()
stemmer = SnowballStemmer('english')

# Read csv example
data = pd.read_csv('abcnews-date-text.csv')
data_text = data[['headline_text']]
data_text['index'] = data_text.index
documents = data_text

documentsLength = len(documents)
print(documentsLength)

documents[:5]

# Simple oss corpus
nltk.download('wordnet')


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

# Brute lemmatizer
pos_list = ['a','s','r','n','v']
def lemmatize_brutal(word):
    for posi in pos_list:
            lemma = lemmatizer.lemmatize(word, pos=posi)
            if lemma is not word:
                break
    return lemma

# Preprocessing bundle
def preprocess_text(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 1:
            result.append(stemmer.stem(lemmatize_brutal(token)))
    return result

# Example lemma-stem-preproc
textexample = 'Studied flew ran swimming jumped lm had whimsical typotron gyroscoped. The quick brown fox jumped over the moon, and ran away with the cow. This is my keyboard, there are many like it... but this one is mine. Run run rUn rUN ruN RuN'
preprocessed_wordlist = preprocess_text(textexample)
for w in preprocessed_wordlist:
    print(w)

# Example document
with open('LDA/Sample.txt', encoding='utf8') as file:
    if os.path.exists('LDA/Sample_Out.txt'):
        os.remove('LDA/Sample_Out.txt')
    fout = open('LDA/Sample_Out.txt', 'a', encoding='utf8')
    contents = '\0'
    while
    try:
        contents = file.readline()
    except:
        pass
    preprocessed_contents = preprocess_text(contents)
    fout.write(contents)
    fout.close()



# # Stemmer example
# stemmer = SnowballStemmer('english')
# original_words = ['caresses', 'flies', 'dies', 'mules', 'denied','died', 'agreed', 'owned', 
#            'humbled', 'sized','meeting', 'stating', 'siezing', 'itemization','sensational', 
#            'traditional', 'reference', 'colonizer','plotted']
# singles = [stemmer.stem(plural) for plural in original_words]
# pd.DataFrame(data = {'original word': original_words, 'stemmed': singles})

# def lemmatize_stemming(text):
#     return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))
# def preprocess(text):
#     result = []
#     for token in gensim.utils.simple_preprocess(text):
#         if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
#             result.append(lemmatize_stemming(token))
#     return result

# doc_sample = documents[documents['index'] == 4310].values[0][0]
# print('original document: ')
# words = []
# for word in doc_sample.split(' '):
#     words.append(word)
# print(words)
# print('\n\n tokenized and lemmatized document: ')
# print(preprocess(doc_sample))










