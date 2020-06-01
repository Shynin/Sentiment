from siteParser import parsed
# import string
import nltk
import re
from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
# from nltk.stem import WordNetLemmatizer

# lemmatizer = WordNetLemmatizer()
stop_words = list(set(stopwords.words('english')))

pos_train = open('../posimdb.txt', encoding='utf-8').read()
neg_train = open('../negimdb.txt', encoding='utf-8').read()
parsed_text = parsed

# removing punctuation with regex
# workData = re.sub(r"[,“–”)(@\'?\.:$%_]", "", text)


def parsedPrep(text):
    work_data = re.sub(r"[,’“–”)(@\'?\.:$%_]", "", text).lower()
    return work_data


def listPrep(text):
    lower_case = text.lower()
    sent_tok = sent_tokenize(lower_case)
    # filtered_sentence = [w for w in sent_tok if not w in stop_words]
    return sent_tok


def dictPrep(words):
    return dict([(word, True) for word in words.split() if word not in stop_words])


posids = listPrep(pos_train)
pos_feats = [(dictPrep(f), 'positive') for f in posids]

negids = listPrep(neg_train)
neg_feats = [(dictPrep(f), 'negative') for f in negids]

trainfeats = pos_feats + neg_feats

parsed_text = parsedPrep(parsed)
test_set = dictPrep(parsed_text)
# print(parsed_text)

# def textCleaner(text):
#     lower_case = text.lower()
#     cleaned_text = lower_case.translate(
#         str.maketrans('', '', string.punctuation))

#     word_tokens = word_tokenize(cleaned_text)
#     filtered_sentence = []
#     lemmatized_words = []

#     filtered_sentence = [w for w in word_tokens if not w in stop_words]
#     lemmatized_words = [lemmatizer.lemmatize(w) for w in word_tokens]
#     return dict([(word, True) for word in lemmatized_words])


# print(textCleaner("I feel very good about these beers"))

# removing stop words
# stop_words = set(stopwords.words('english'))
# workData = ' '.join(
#     [word for word in workData.split() if word not in stop_words])

# pos_trainset = textCleaner(pos_train)
# neg_trainset = textCleaner(neg_train)
# parsed_set = textCleaner(parsed_text)
