import pandas as pd


FROM_FILE = 'reviews.csv.gz'
TEXT_COL_NAME = 'comments'
TO_FILE = 'review_data.csv'

def clean_data(FROM_FILE,TO_FILE):
  # After uploading .gz file, open and clean with pandas 
  dfPandas = pd.read_csv(FROM_FILE, compression='gzip')
  dfPandas = dfPandas.dropna()
  dfPandas[TEXT_COL_NAME] = dfPandas[TEXT_COL_NAME].map(
      lambda x:x.replace('\n','').replace('\r',''))
  dfPandas.to_csv(TO_FILE, index=False)


if __name__ == "__main__":

  clean_data(FROM_FILE, TO_FILE)