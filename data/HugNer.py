from ckip_transformers.nlp import CkipWordSegmenter, CkipPosTagger, CkipNerChunker

class HugBert():
    def __init__(self):
        # self.ws_driver  = CkipWordSegmenter(model="bert-base") # 分词
        # self.pos_driver = CkipPosTagger(model="bert-base")     # 词性标注 
        self.ner_driver = CkipNerChunker(model="albert-base")
    
    def ner(self,text):
        nlp = self.ner_driver([text],show_progress = False)
        org_fac_words = [token.word.replace(" ",'') for token in nlp[0] if token.ner in ['ORG', 'FAC','LOC']]
        return set(org_fac_words)