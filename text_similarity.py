import gensim
from gensim.models.doc2vec import TaggedDocument
import nltk
from nltk.corpus import stopwords
import os

#The program helps you compare a number of files to a certain file and find how similar they are.

directory='NAME_OF_DIRECTORY_WHERE_YOU_KEEP_YOUR_FILES_TO_COMPARE'
stopwords_en=stopwords.words('english')

#reading all the files in the directory. This assumes you have ONLY the files you want to compare in your directory
files=[]
for i in os.listdir(directory):
    if i.endswith('.txt'):
        files.append(i)

#text preprocessing function. Basic processing only here, for the sake of current example.
def preprocessing(raw):
    f=open(raw, 'r', encoding='utf8').read()
    wordlist=nltk.word_tokenize(f)
    text=[w.lower() for w in wordlist if w not in stopwords_en]
    return text

#initializing the list of TaggedDocs to be used in the Gensim model, and building it
taggeddocs=[]

for i in files:
    file_name=directory+i
    text=preprocessing(file_name)
    model_doc=TaggedDocument(words=text, tags=[i])
    taggeddocs.append(model_doc)

#initializing the gensim model and training it
model=gensim.models.Doc2Vec(taggeddocs, dm=0, alpha=0.025, vector_size=20, min_alpha=0.025, min_count=0)
model.train(taggeddocs, total_examples=model.corpus_count, epochs=80)

print(model.docvecs.most_similar('NAME_OF_THE_FILE_TO_COMPARE_AGAINST'))
