import textblob
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

### get the file to classify
file=open(YOUR_FILE_HERE).read()


### the training set
train = [
         ('Organic revenue was up for the quarter and year-to-date with operating margin expansion in most of the sectors.', 'pos'),
         ('This improvement is being driven by the strength of our year-to-date results, coupled with an improved outlook on foreign exchange impact.', 'pos'),
         ('Our largest market in the region, had high single-digit organic revenue growth.', 'pos'),
         ('We are pleased with the progress weare making in the e-commerce channels.', 'pos'),
         ('Increased demand for hybrid cloud technologies contributed to accelerated revenue, operating income and cash flow growth.', 'pos'),
         ('Our services revenue also exceeded our growth expectations.', 'pos'),
         ('We are modestly raising our non-GAAP operating margin.', 'pos'),
         ('We are also raising our full year non-GAAP earnings per share outlook.', 'pos'),
         ('It did really well this quarter in bringing through a lot of operating margin well ahead of our expectations and consumer expectations.', 'pos'),
         ('We will be able to capture those revenue synergies relatively quickly.', 'pos'),
         ('Our shared gains have been accelerating.', 'pos'),
         ('We continue to capture market share at high rates.', 'pos'),
         ('You have seen some volume pressure in the quarter.', 'neg'),
         ('That shows year-over-year deceleration in earnings.', 'neg'),
         ('Some markets remained challenged and underperformed the remaining parts of the country.', 'neg'),
         ('Our sales have been slower than we would have thought due to poor performance.', 'neg'),
         ('Our initiative did not generate the benefits yet that we expected.', 'neg'),
         ('Our overall commercial sales growth has declined as well.', 'neg'),
         ('We faced several other pressure points.', 'neg'),
         ('We have experienced accelerated pressure on wages significantly more than I have experienced in the past.', 'neg'),
         ('These factors have significantly hampered our earnings per share growth.', 'neg'),
         ('We unfortunately experienced a disproportionate amount of them working against us.', 'neg'),
         ('We are disappointed in our revenue results and guidance for the balance of the year.', 'neg'),
         ('The impact from these issues is lower productivity.', 'neg')
         ]

### creating the training classifiers
cl = NaiveBayesClassifier(train)
file_s=TextBlob(file)


print(cl.classify(file))
print(file_s.sentiment)





