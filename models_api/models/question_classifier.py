import json
from sentence_transformers import SentenceTransformer, util
#from fuzzywuzzy import fuzz
#import pymorphy2


class FAQClassifier():
    def __init__(self):
        #self.morph = pymorphy2.MorphAnalyzer()
        with open("faq.json") as json_file:
            self.faq = json.load(json_file)
        self.model = SentenceTransformer("cointegrated/rubert-tiny2")
        self.questions = list(self.faq.keys())
        self.question_embeds = self.model.encode(self.questions)

    def classify_question(self, text):

        query_embed = self.model.encode([text])
        cos_sim = util.cos_sim(query_embed, self.question_embeds)

        max_sim_idx = max(enumerate(cos_sim[0]),key=lambda x: x[1])[0]

        answer = self.faq[self.questions[max_sim_idx]]


        #text = ' '.join(self.morph.parse(word)[0].normal_form for word in text.split())
        #questions = list(self.faq.keys())
        #scores = list()

        #for question in questions:
        #    norm_question = ' '.join(self.morph.parse(word)[0].normal_form for word in question.split())
        #    scores.append(fuzz.token_sort_ratio(norm_question.lower(), text.lower()))

        #answer = self.faq[questions[scores.index(max(scores))]]

        return answer

