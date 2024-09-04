from nltk.corpus import stopwords
import nltk
import re
nltk.download('punkt')
nltk.download('stopwords')

from collections import Counter

def get_tokens():
   with open('FirstContactWithTensorFlow.txt', 'r') as tf:
    text = tf.read()
    # lowercase text
    lowers = text.lower()
    # remove punctuation using regex
    no_punctuation = re.sub(r'[^\w\s]', ' ', lowers)
    tokens = nltk.word_tokenize(no_punctuation)
    # the lambda expression below this comment
    # stores stopwords in a variable for eficiency:
    # it avoids retrieving them from ntlk for each iteration
    sw = stopwords.words('english')
    filtered = [w for w in tokens if not w in sw]
    return filtered

tokens = get_tokens()
count = Counter(tokens)

print("10 most common words without punctuation and stop words")
print("=====")
for word, freq in count.most_common(10):
    print("\'{}\' —".format(word), freq)

print("\n=====")
print("Total number of words:", len(tokens))