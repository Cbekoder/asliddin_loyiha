import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BAZA_PATH = os.path.join(BASE_DIR, "files", "baza.csv")
EDIT_PATH = os.path.join(BASE_DIR, "files", "full.edit.csv")


baza_scores = pd.read_csv(BAZA_PATH).set_index("Text")["Score"].to_dict()
edit_scores = pd.read_csv(EDIT_PATH).set_index("Text")["Score"].to_dict()

def get_score(text):
    
    return edit_scores.get(text, baza_scores.get(text, "Not Found"))

