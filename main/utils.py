import pandas as pd

baza_scores = pd.read_csv("files/baza.csv").set_index("Text")["Score"].to_dict()
edit_scores = pd.read_csv("files/full.edit.csv").set_index("Text")["Score"].to_dict()

def get_score(text):
    
    return edit_scores.get(text, baza_scores.get(text, "Not Found"))

