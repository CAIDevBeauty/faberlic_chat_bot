import json

from sentence_transformers import SentenceTransformer, util

# from fuzzywuzzy import fuzz
# import pymorphy2


class FAQClassifier:
    def __init__(self):
        with open("faq.json") as json_file:
            self.faq = json.load(json_file)
        self.model = SentenceTransformer("cointegrated/rubert-tiny2")
        self.questions = list(self.faq.keys())
        self.question_embeds = self.model.encode(self.questions)

    def classify_question(self, text):
        query_embed = self.model.encode([text])
        cos_sim = util.cos_sim(query_embed, self.question_embeds)

        max_sim_idx = max(enumerate(cos_sim[0]), key=lambda x: x[1])[0]

        answer = self.faq[self.questions[max_sim_idx]]

        return answer
