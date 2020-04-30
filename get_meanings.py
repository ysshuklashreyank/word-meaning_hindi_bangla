# Importing the necessary libraries
import pandas as pd
import googletrans
from googletrans import Translator
# from vocabulary.vocabulary import Vocabulary as vb

# Reading and storing the CSV file as a dataframe
df = pd.read_csv('input.csv', names = ["Word", "Meaning", "Hindi", "Bangla"])
# df.head(20)

translator = Translator()
# for row in df:
  # print(row)
for i in range(len(df)):
  # print(df.iloc[i,0]
  df.iloc[i,2] = translator.translate(df.iloc[i,0], dest = "hi").text
  df.iloc[i,3] = translator.translate(df.iloc[i,0], dest = "bn").text
  # df.iloc[i,1] = translator.translate(df.iloc[i,0], dest = "en").text
df
df.to_csv("out.csv")

    