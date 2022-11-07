# PolyFinances

To run the econometrics model use the modelPrediction.ipynb file

All the variables used within the file are contained in data/dataset/final2.csv

External sources of data used in our model:
- Bank of Canada (web scrapping to extract more press releases) (see web_scrape.ipynb and data/dataset/can_statements.json)
- FRED (through its open source API) (see analysis.ipynb and var_exp_df.ipynb)
- Bank of Canada (historic govt yield for different maturities see data/dataset/cadbond.csv)

We attempted to collect more data, but often the risk-reward of taking the time to collect and clean this data simply didn't make sense

Our major findings, following the best practices for building models for timeseries, is that over a 2 week period a NLP model nor an econometrics model have much value.
However using a makeshift technique, using PCA, Linear Regression and the Random Forest Regressor (and using our NLP variables and more general variables) we've found that our model has modest predictive power for volatility over a 2 week period. This predictive power remains minute, however we believe that with more time some of our findings could blossom into an applicable predictive model, namely for risk minimization, regarding currency fluctuation. For instance, this forecast could be used to value derivatives on USD/CAD which could have its applications in hedging, for canadian corporations trading with the US and holding opposing currencies for a timeframe of around 2 weeks.

We've enjoyed this project thorougly, thank you for your near perfect organization of the event!


### Planning and scibles
Repo de polyfinance (données) :
- https://github.com/PolyFinances/Datathon-2022-data

Quelques repos très intéressants : 

- https://github.com/davidjsmith44/NLP-Fed-Speeches
- https://github.com/kathrinv/what-do-you-mean
- https://github.com/usydnlp/FedNLP

1-Find a way to filter the csvs for Bank of Canada and Fed (spacy or nltk)

2-From the filtered data, figure out which variables are necessarry for finBert

3-Build Econo model based on
  Influence of present news on current macro state
  Variance and Implied Volatility
  
  
