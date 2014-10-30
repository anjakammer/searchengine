from sklearn.feature_extraction import stop_words


class Normalizer:
    text = ""
    stopwords = []
    def __init__(self, text):
        self.text = text.lower()
        with open('stopwoerter.txt') as f:
            self.stopwords = [word.strip('\n') for word in f.readlines()]

    def getTokens(self):
        return self.text.split(" ")

