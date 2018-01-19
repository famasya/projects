import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neural_network import MLPClassifier


from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm


input_data = pd.read_csv('data1.tsv', delimiter='\t')
sentence = input_data['sentence']
label = input_data['label']
cv = CountVectorizer()
model = MLPClassifier()

from sklearn.pipeline import Pipeline
pipeline = Pipeline([
    ('vect', CountVectorizer()),
    ('clf', model),
])
pipe.fit(sentence, label)

pipe.predict(['Hei I am sad'])
pipe.predict(['you are worst'])
