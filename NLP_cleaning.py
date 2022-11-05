#%%
import pandas as pd
import numpy as np
import re
import time
    # data analysis
import numpy as np
import pandas as pd
import pickle
from tqdm import tqdm_notebook as tqdm
    # natural language processing - NLTK
import nltk
from nltk.corpus import wordnet, stopwords
from nltk.probability import FreqDist
from nltk.stem import WordNetLemmatizer
    # natural language processing - Gensim and LDA
import gensim
from gensim import corpora, models, similarities
from gensim.models import CoherenceModel
    # natural language processing - TextBlob (Sentiment)
from textblob import TextBlob
    # data visualization
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns



#%%

def read_data(filename: str) -> pd.DataFrame:
    return pd.read_csv(f"data/dataset/{filename}.csv",
                       index_col=0, parse_dates=True)

df_statement = read_data("FOMC/statement")
df_speech = read_data("FOMC/speech")
df_testimony = read_data("FOMC/testimony")


#%%



#%%


#%%




#%%

#%%
#%%
#%%




#%%

#%%
#%%
#%%




#%%

#%%
#%%