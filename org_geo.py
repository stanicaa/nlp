import spacy
import nltk

nlp = spacy.load('en_core_web_sm')

file= 'YOUR_FILE_HERE'
text=open(file).read()
sentences=nltk.sent_tokenize(text)

organizations=[]
geography=[]

for i in range(len(sentences)):
    doc=nlp(sentences[i])
    for j in doc.ents:
        if j.label_=='ORG':
           organizations.append(j.text)
        if j.label_=='GPE':
           geography.append(j.text)

organizations=set(organizations)
geography=set(geography)

print('These are the mentioned organizations', organizations)
print('These are the metioned gepgraphical names', geography)
