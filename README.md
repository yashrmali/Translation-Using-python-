# 🌐Translation Using python 

This Python script translates text from Hindi to English using the Google Translate API and replaces the original text in a CSV file.

## 🔧Requirements

- Python 3.x
- pandas library
- googletrans library

Install the required libraries using pip:

```bash
pip install pandas googletrans==4.0.0-rc1
```
## 🚀Usage
1.Clone the repository or download the script.

2.Make sure you have installed the required libraries.

3.Prepare a CSV file containing text in Hindi (e.g., hindi.csv).

4.Run the script using the following command:
```bash
python translator.py
```
The script will translate the text in the CSV file from Hindi to English and display the translated DataFrame.

📝Examples

Suppose you have a CSV file named `hindi.csv` with the following contents:
|    | Column 1 | Column 2 |
|----|----------|----------|
| 0  | नमस्ते   | कैसे हो   |
| 1  | क्या हाल है | बहुत अच्छा है |

After running the script, the translated DataFrame will be displayed:

|    | Column 1 | Column 2   |
|----|----------|------------|
| 0  | Hello    | How are you? |
| 1  | How are you? | Very good |

Thank you for exploring this project!

