import re
from nltk.corpus import stopwords

special_character_removal=re.compile(r'[^a-z\d ]',re.IGNORECASE)
replace_numbers=re.compile(r'\d+',re.IGNORECASE)
    
def clean_text(text):
    text = text.lower()
    text = re.sub(r"what's", "what is ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"\'ve", " have ", text)
    text = re.sub(r"can't", "cannot ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"i'm", "i am ", text)
    text = re.sub(r"i’m", "i am", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub(r",", " ", text)
    text = re.sub(r"\.", " ", text)
    text = re.sub(r"'", " ", text)
    text = replace_numbers.sub('', text)
    text = str(text).replace("\n", " ")
    text = str(text).replace("   ", " ")
    text = special_character_removal.sub('',text)
    
    if stop_words: # stop_word read from file and stop_word dictionary read from file
        text = text.split()
        #check for stopwords and remove
        text = [word for word in text if not word in set(stopwords.words('english'))]
        #back to string
        text = ' '.join(text)
    return text
def clean_dataframe(df):
    list_sentences = df["comment_text"].values
    df['clean_comments'] = pd.Series([clean_text(text) for text in list_sentences])
    return df
