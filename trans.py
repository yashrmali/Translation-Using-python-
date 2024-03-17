import pandas as pd
from googletrans import Translator

# Load the CSV file into a DataFrame
data = pd.read_csv("C:/py pg/Translation Hindi to English/hindi.csv")

# Display the original DataFrame
print("Original DataFrame:")
print(data)

# Initialize the translator
translator = Translator()
translations = {}

# Translate unique elements in each column
for column in data.columns:
    unique = data[column].unique()
    for element in unique:
        translations[element] = translator.translate(element, src='hi', dest='en').text

# Replace original elements with translations in the DataFrame
data.replace(translations, inplace=True)

# Display the DataFrame with translations
print("\nDataFrame with Translations:")
print(data)
