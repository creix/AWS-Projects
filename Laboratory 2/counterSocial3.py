import string
from collections import Counter
import requests
import json
from Tweet_Tokenizer import preprocess
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')

# Fetch the status
response = requests.get('https://Counter.Social/api/v1/timelines/public')
responses = json.loads(response.text)

print('------------- TWEET ANALYSIS -------------')

# Tokenize the content of the status
tokens = []
for item in responses:
    print(item['content'])
    tokens = tokens + preprocess(item['content'])

count = Counter(tokens)
print(count.most_common(20))

# Remove stop words, punctuation and HTML tags
punctuation = list(string.punctuation)
sw = stopwords.words('english') + punctuation + ['<p>', '</p>', '<br />', '<span>', '</span>', '<a>', '</a>', 'apos', 'quot']

filtered = [w for w in tokens if not w in sw]
count = Counter(filtered)

print("REMOVED STOP WORDS")
print(count.most_common(20))