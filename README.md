# nlp
Various NLP examples. This is a vast area, current repository is meant to only provide simple examples to prove capabilities to get you started on learning the libraries. There is no such thing as out of the box solution, so it really depends on what your goal is. The main libraries we highly recommend learning are: nltk (to get started), spacy (excellent library) and gensim (the workhorse for vector models), tensorflow (for neural network based models like seq2seq and so on). There are a lot more libraries out there, and we will flag some of them below as we use them.

ORG_GEO.PY
- Example of using nltk and spacy libraries to identify and get the organizations and geographic names from a text.
- NOTE: there is actually no particular need for nltk here, spacy can do the tokenizing too. So it is actually an overkill to use both libraries. 
- You can do a lot more with spacy, check https://spacy.io/ .
- Same with nltk. Check https://www.nltk.org/ .

blob_NaiveBayes.py
- Exercise for understandign NaiveBayes classifiers. This example is purely an exercise. In this particular case, I was playign with company transcripts. We are using TextBlob here, https://textblob.readthedocs.io/en/dev/index.html, a very good library for simple tasks.
- Why just an exercise? Because we find NaiveBayes classifiers to be actually very naive, and testing did not find it good enough. For building stronger classifiers, we strongly recommend doing deeper work/research on scikit.learn and tensorflow libraries.

basic_text_analysis.py
- this is a basic example of how to build your own word2vec models, how to preprocess the text and keep only specific type of words, like nouns, as well as frequency analysis of the text. It is using gensim, spacy and nltk libraries. For deeper understanding of the libraries, please check below.
- gensim @ https://radimrehurek.com/gensim/
- spacy at https://spacy.io/
- nltk @ https://www.nltk.org/

text_similarity.py
- program helps compare multiple files to a certain base file and find out how similar they are.
- the NLP parsing function (text processing function) is basic here, but you can replace it with more advanced versions, depending on what your needs are.
- library used: gensim, nltk


