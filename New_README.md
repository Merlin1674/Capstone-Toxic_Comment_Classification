# Empower Fruitful Discissions 
Classifying toxicity in online communication

LOGO

This repository presents a solution to Jigsaw's [Toxic Comment Classification Challenge](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge) on kaggle.com. The project was carried out after the official deadline of the challenge in February 2022 and is therefore to be taken as out of competition. 

# Environment

In order to use the code set up a python environment with help of the requirements.txt file in this repository. For this you can either use make setup or the following commands:

´´´python 
pyenv local 3.9.4
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
´´´

# Exploratory Data Analysis

The data for the challenge consists of ca. 160k comments from Wikipedia that was labelled by humans in 6 different classes: toxic, severe toxic, obscene, threat, insult and identity hate. Furthermore, the data set shows a great imbalance with about 90% of comments showing no sign of toxicity and therefore belonging to none of the above mentioned classes. The get more detailed insights into the data set please refer to the [EDA-notebook](LINK). 


# Preprocessing

To clean the data please use the [Clean Function Notebook](LINK) in the preprocessing folder. There you have the option to clean the data from all unwanted special characters, stopwords or short forms like I'm, aren't etc. In addition to that, you will find code for lemmatization and stemming.

# Data Augmentation

In order to augment the data set to tackle the imbalance between the classes, different measures were taken. In the preprocessing folder you will find code for e.g. Synonym Replacement and Backtranslation.

# Model

The models folder gives an overview of the different models we trained to deal with this challenge. You will find examples for BERT, RoBERTa, a BiLSTM-CNN hybrid and a BiLSTM with attention layers. 

# Results

Our best performing model is based on the transformer RoBERTa and scored with a 0.98...  the ROC-AUC metric that was asked for in the challenge. In terms of preprocessing, it turns out that simply cleaning the data without the extraction of stop words or the use of lemmatization gave us the best results. Moreover, none of the data augmentation strategies that we used resulted in a further improvement of the score. 

Obviously, as is true for any time limited project, there is always more that could be done. Our Error Analysis shows that more data or pseudo-labelling would help to improve the score.

# Authors

This repository was created by Katharina Neumüller, Ksenia Gerasimovich, Daniel Guhr and Kristin Stöcker, participants of the Data Science and Machine Learning boot camp of neue fische Gmbh that took place from Nov 29, 2021, to Feb 25, 2022. It documents their final project that was carried out over the last four weeks of their training.

# License

This repository is published under the MIT License.