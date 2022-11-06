# %%
import pandas as pd
import numpy as np
from tabulate import tabulate



# %%
df=pd.read_csv("D:\Datachallenge\PolyFinances\data\dataset\FOMC\statement.csv")



# %%



# %%
def dropfill(text):
    string=text.replace("\r\n", "").replace("\r", "").replace("\n", "");
    newstring=string.replace("[SECTION]","")
    return(newstring)

# %%
df["contents"]=df["contents"].apply(dropfill)
df.drop_duplicates(subset=["contents"])


# %%
from transformers import BertForSequenceClassification, BertTokenizer
import torch 
import pandas as pd
import numpy as np
from transformers import pipeline
import scipy
tokenizer=BertTokenizer.from_pretrained("ProsusAI/finbert")
model= BertForSequenceClassification.from_pretrained("ProsusAI/finbert",num_labels=3)
def betoken(text):
    inputs = tokenizer(text, return_tensors="pt",max_length=511)
    with torch.no_grad():
        logits = model(**inputs).logits
    scores = {k: v for k, v in zip(model.config.id2label.values(), scipy.special.softmax(logits.numpy().squeeze()))}
    out=scores.get("positive")+scores.get("negative")*-1
    return(out)
        


df["sentiment"]=df["contents"].apply(betoken)
df.to_csv("FedStatements.csv")