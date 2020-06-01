from textPrepocessing import trainfeats, test_set
import nltk
from nltk.classify import NaiveBayesClassifier
# from nltk.corpus import stopwords
# stopset = list(set(stopwords.words('english')))

# print(test_set)

# def word_feats(words):
#     return dict([(word, True) for word in words.split() if word not in stopset])


# posids = ['I love this sandwich.', 'I feel very good about these beers.']
# pos_feats = [(word_feats(f), 'positive') for f in posids]

# negids = ['I hate this sandwich.', 'I feel worst about these beers.']
# neg_feats = [(word_feats(f), 'negative') for f in negids]
# # print(pos_feats)
# # print(neg_feats)
# trainfeats = pos_feats + neg_feats
classifier = NaiveBayesClassifier.train(trainfeats)

# print(test_set)
print(classifier.classify(test_set))
print("With accuracy:",
      (NaiveBayesClassifier.classify.accuracy()
# print(nltk.classify.accuracy(classifier, test_set))


# print(word_feats(posids))
