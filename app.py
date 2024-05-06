import tkinter as tk
from tkinter import ttk
from googletrans import Translator
from textblob import TextBlob

def translate_text(text, target_lang='en'):
    try:
        translator = Translator()
        translated_text = translator.translate(text, dest=target_lang)
        return translated_text.text
    except Exception as e:
        print("Translation error:", e)
        return "Translation Error"


def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0:
        return 'Positive'
    elif sentiment_score < 0:
        return 'Negative'
    else:
        return 'Neutral'

def cross_lingual_sentiment_analysis():
    input_text = text_entry.get("1.0", tk.END).strip()
    source_lang = source_lang_entry.get()
    target_lang = target_lang_entry.get()

    if source_lang != 'en':
        translated_text = translate_text(input_text, target_lang)
    else:
        translated_text = input_text

    sentiment = analyze_sentiment(translated_text)
    result_label.config(text="Sentiment: " + sentiment)

#  GUI
root = tk.Tk()
root.title("Sentinex")

# window size and position
window_width = 600
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

# Text Input
text_label = ttk.Label(root, text="Enter Text:", font=("Helvetica", 14))
text_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
text_entry = tk.Text(root, height=5, width=50, font=("Helvetica", 12))
text_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

# Source Language
source_lang_label = ttk.Label(root, text="Source Language:", font=("Helvetica", 14))
source_lang_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
source_lang_entry = ttk.Entry(root, font=("Helvetica", 12))
source_lang_entry.grid(row=3, column=0, padx=10, pady=5, sticky="ew")

# Target Language
target_lang_label = ttk.Label(root, text="Target Language:", font=("Helvetica", 14))
target_lang_label.grid(row=2, column=1, padx=10, pady=10, sticky="w")
target_lang_entry = ttk.Entry(root, font=("Helvetica", 12))
target_lang_entry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

# Analyze Button
analyze_button = ttk.Button(root, text="Analyze", command=cross_lingual_sentiment_analysis, style='Accent.TButton')
analyze_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# Result Label
result_label = ttk.Label(root, text="", font=("Helvetica", 14))
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.update_idletasks()
root.mainloop()
