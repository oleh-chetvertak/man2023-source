import nltk, string, pymorphy3
from nltk import pos_tag
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import codecs, random, os

nltk.data.path.extend(["C:\\front end 13 08\\djangoMAN/nltk_data", "/home/olegchetvertak/man2023-source/nltk_data"])

morph = pymorphy3.MorphAnalyzer(lang='uk')
stopwords = stopwords.words("ukrainian")

SIA = SentimentIntensityAnalyzer('sentiment/vader_lexicon/vader_lexicon.txt')
stop_words = frozenset(stopwords + list(string.punctuation))


class NLTKAnalyse:
    def __init__(self, data, with_file, min_ton, max_ton):
        self.sentences = []
        self.aver_polarity = 0
        self.aver_percent = 0
        self.min = min_ton
        self.max = max_ton
        self.withFile = with_file
        self.data = data

    def filter_text(self):
        randkey = random.randint(100000, 999999)
        if self.withFile:
            with open(f"{randkey}.txt", "wb+") as file:
                for chunk in self.data.chunks():
                    file.write(chunk)
            file = codecs.open(f"{randkey}.txt", "r", "utf-8")
            parts = file.read().splitlines()
            for elem in parts:
                self.sentences.extend(sent_tokenize(elem))
            file.close()
            os.remove(f"{randkey}.txt")
        else:
            self.sentences = sent_tokenize(self.data)

    def at_start(self):
        self.filter_text()

    def get_every_analyse(self):
        totalY = [0 for _ in range(-100, 101, 10)]
        totalX = [f'{i} %' for i in range(-100, 101, 10)]
        all_polarities = []
        for sentence in self.sentences:
            words = word_tokenize(sentence)
            without_stop_words = [word for word in words if word not in stop_words]
            normal_words = []
            for token in without_stop_words:
                p = morph.parse(token)[0]
                normal_words.append(p.normal_form)

            polarity = round(SIA.polarity_scores(' '.join(normal_words))["compound"]*10)*10
            if int(self.max) >= int(polarity) >= int(self.min):
                totalY[totalX.index(f'{polarity} %')] += 1
            all_polarities.append(polarity)

        if len(all_polarities) != 0:
            self.aver_polarity = sum(all_polarities)/(len(all_polarities)*100)
        else:
            self.aver_polarity = 0
        self.aver_percent = self.aver_polarity * 100
        return totalX, totalY
