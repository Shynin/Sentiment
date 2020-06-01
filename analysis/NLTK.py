import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from textPrepocessing import parsed_text
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# text = open('../read.txt', encoding='utf-8').read()
# lower_case = text.lower()
# cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

tokenized_words = word_tokenize(parsed_text)
rem_stopW = [w for w in tokenized_words if not w in stop_words]
final_words = [lemmatizer.lemmatize(w) for w in rem_stopW]


emotion_list = []

# for word in tokenized_words:
#     if word not in stopwords.words('english'):
#         final_words.append(word)

with open('../emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace('\n', '').replace(
            ',', '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)

print(emotion_list)

w = Counter(emotion_list)
print(w)


def sentiment_analyze(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    print(score)
    # neu = score['neu']
    # neg = score['neg']
    # pos = score['pos']
    # if neg > pos and neg > neu:
    #     print("Negative Sentiment: " + str(neg * 100) + "%")
    # elif pos > neg and pos > neu:
    #     print("Positive Sentiment: " + str(pos * 100) + "%")
    # else:
    #     print("Neutral Vibe: " + str(neu * 100) + "%")


# foranalyze = ' '.join(final_words)
# sentiment_analyze(foranalyze)

# fig, ax1 = plt.subplots()
# ax1.bar(w.keys(), w.values())
# fig.autofmt_xdate()
# plt.savefig('graph.png')
# plt.show()
