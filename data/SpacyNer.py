import spacy
from spacy.pipeline import EntityRuler

class SpacyNer:
    def __init__(self):
        self.nlp = spacy.load("zh_core_web_trf")
        self.patterns = self.get_patterns()

    def get_patterns(self):
        # 读取txt文件内容
        scene_patterns = []
        with open('/kaggle/input/tourner/hotel_set.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
        for line in lines:
            scene_dict = {"label": "FAC", "pattern": line.strip()}
            scene_patterns.append(scene_dict)
        with open('/kaggle/input/tourner/scenic_set.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
        for line in lines:
            scene_dict = {"label": "FAC", "pattern": line.strip()}
            scene_patterns.append(scene_dict)
        with open('/kaggle/input/tourner/canteen_set.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
        for line in lines:
            scene_dict = {"label": "FAC", "pattern": line.strip()}
            scene_patterns.append(scene_dict)
        return scene_patterns
    
    def addpipe(self,pipe):
        ruler = self.nlp.add_pipe(pipe)
        ruler.add_patterns(self.patterns)

    def spacy_ner(self, text):
        entities = set()
        doc = self.nlp(text)
        for ent in doc.ents:
            # 判断是否为"LOC", "ORG", "FAC"中的某一个
            if ent.label_ in ["LOC", "ORG", "FAC"]:
                # Append the entity text to the list
                entities.add(ent.text.replace(" ",''))
        return entities