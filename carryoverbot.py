import pandas as pd
import numpy as np
import math
finalcsv=pd.read_csv("D:\Datachallenge\PolyFinances\data\dataset\\final.csv")
cadlist=finalcsv["can_sentiment"]
usfedstatement=finalcsv["us_fed_sentiment"].tolist()
usfedspeech=finalcsv["fed_speech_sentiment"].tolist()
usmlist=finalcsv["fed_minutes_sentiment"].tolist()
canlist=finalcsv["can_sentiment"].tolist()

bool=0
constant=0.5
for j in usfedspeech:
    if j==0 and bool!=0:
        newfetch=usfedspeech[bool-1]*constant
        if math.sqrt(newfetch**2)<0.00001:
            newfetch=0

        usfedspeech[bool]=newfetch



    bool+=1
bool2=0
for j in usfedstatement:
    if j==0 and bool2!=0:
        newfetch=usfedstatement[bool2-1]*constant
        if math.sqrt(newfetch**2)<0.00001:
            newfetch=0

        usfedstatement[bool2]=newfetch
    


    bool2+=1
bool3=0
for j in usmlist:
    if j==0 and bool3!=0:
        unewfetch=usmlist[bool3-1]*constant
        if math.sqrt(unewfetch**2)<0.00001:
            unewfetch=0

        usmlist[bool3]=unewfetch
    


    bool3+=1
bool4=0
for j in canlist:
    if j==0 and bool4!=0:
        unewfetch=canlist[bool4-1]*constant
        if math.sqrt(unewfetch**2)<0.00001:
            unewfetch=0

        canlist[bool4]=unewfetch
    


    bool4+=1
finalcsv["carryover(usfedspeech)"]=usfedspeech
finalcsv["carryover(usfedstatement"]=usfedstatement
finalcsv["carryover(usfedminutes)"]=usmlist   
finalcsv["carryover(canStatement"]=canlist 

finalcsv.to_csv("finalcsv2.csv")

# for j in usfedspeech:

newcsv=pd.read_csv("D:\Datachallenge\PolyFinances\\finalcsv2.csv")
print(newcsv)


# femd=pd.DataFrame()
# femd["date"]=fedm["date"]
# femd["sentiment(femd)"]=fedm["sentiment"]
# def add_sentiment(date):
#     findrow=fedm.loc[fedm["date"]==date]
#     sentimentvalue=findrow["sentiment"]

# finalcsv["femdsentiment"]=finalcsv["date"].apply(add_sentiment)

# finalcsv.to_csv("Finaltry.csv")
