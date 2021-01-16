from sparknlp.annotator import *
from sparknlp.common import *
from sparknlp.base import *
import sparknlp


INPUT_FILE = "review_data.csv"
INPUT_COLUMN= "comments"
RESULT_FILE = "results.csv"


def read_csv(input_file):
  """Load data from .csv file into spark dataframe
  """
  spark = sparknlp.start()
  spark.sparkContext.addFile(input_file)
  dfSpark = spark.read.csv(input_file, header=True)
  return dfSpark

def predict_language(data, input_column):
  """Predict the language for text in desitnated input column
  and return the dataframe with output in 'language' column
  """
  documentAssembler = DocumentAssembler()\
    .setInputCol(input_column)\
    .setOutputCol("document")

  # Detect language
  detectLanguage = LanguageDetectorDL()\
    .pretrained('ld_wiki_20',lang='xx')\
    .setInputCols([input_column])\
    .setOutputCol('language')\
    .setCoalesceSentences(False)\
    .setThreshold(.3)

  # Transform data 
  dfAssembled = documentAssembler.transform(dfSpark)
  dfResults = detectLanguage.transform(dfAssembled)

  return dfResults




if __name__ == "__main__":
  
  # Read data
  data = read_csv(INPUT_FILE)
  
  # Predict language
  results = predict_language(data, INPUT_COLUMN)
  
  # Write results
  data.write.csv(RESULT_FILE)