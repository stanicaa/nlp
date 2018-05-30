import gensim
import nltk
import spacy
from stop_words import get_stop_words
from gensim.models import Word2Vec

#accessing the file
filename='YOUR_FILE_PATH_HERE'
raw=open(filename, 'r').read()

#keeping only NOUN, PNOUN here. You can always add more, like ADJ, VERB, ADV to analyze it
def text_pos(raw):
    sentences=nltk.sent_tokenize(raw)
    nlp = spacy.load('en_core_web_sm')
    vector=[]
    for i in range(len(sentences)):
        doc=nlp(sentences[i])
        sent=[w for w in doc if w.pos_ in ['NOUN', 'PROPN']]
        sent=str(sent)
        sent=sent[1:-1]+'.'
        vector.append(sent)
    raw=' '.join(vector)
    raw=str(raw)
    return raw

raw=text_pos(raw)

#preparing the doc for creating a W2V model
sentences=nltk.sent_tokenize(raw)
sentences=[nltk.word_tokenize(sent) for sent in sentences]

#getting rid of the stopwords (Can add getting rid of more stuff here)
en_stop = get_stop_words('en')
for i in range(len(sentences)):
    sentences[i]=[w for w in sentences[i] if w not in en_stop]

#creatign the model. Min_count here sets the minimum word frequency to be considered
model = Word2Vec(sentences, min_count=0, size=500)

r1=model.most_similar(['growth'], topn=40)
print('-------GROWTH')
print(r1)
r2=model.most_similar(['company'], topn=40)
print('------COMPANY')
print(r2)
print('------------- BUSINESS')
print(model.most_similar(['business'], topn=40))

#Simple frequency analysis

tokens=nltk.word_tokenize(raw)
text=nltk.Text(tokens)
fd=nltk.FreqDist(text)
print(fd.most_common(100))
