import nltk
nltk.download('punkt')
import re

from collections import Counter

def get_tokens():
   with open('FirstContactWithTensorFlow.txt', 'r') as tf:
    text = tf.read()
    tokens = nltk.word_tokenize(text)
    return tokens

tokens = get_tokens()
count = Counter(tokens)

print("10 most common words")
print("=====")
for word, freq in count.most_common(10):
    print("\'{}\' —".format(word), freq)

print("\n=====")
print("Total number of words:", len(tokens))