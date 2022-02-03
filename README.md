# Capstone-Toxic_Comment_Classification
Repository of our Capstone project at cgn-ds-21-3

![2845825](https://user-images.githubusercontent.com/94843155/152152295-9fd051e6-a8c0-4a1c-8e7f-546e6b155109.png)


<a href="https://www.flaticon.com/free-icons/natural-language-processing" title="natural language processing icons">Natural language processing icons created by Eucalyp - Flaticon</a>

## !!! This project is still under development !!!

Based on the data set of the Kaggle-Challenge "Toxic Comment Classification - Identify and classify toxic online comments" (https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/overview) we are doing EDA and creating a NLP-model to classify the given comments into the classes "toxic", "severe toxic", "threat", "insult", "obscene" and "identity hate". Some of the comments can have more than one label. According to the Kaggle-challenge requirements the evaluation metric shall be ROC AUC.

## Environment

Use the [requirements](requirements.txt) file in this repo to create a new environment. For this you can either use `make setup` or the following commands:

```BASH
pyenv local 3.9.4
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Authors
Ksenia Gerasimovich, Katharina Neumüller, Kristin Stöcker, Daniel Guhr - participants of the data science bootcamp at neue fische from December 2021 to February 2022

## License
CC-SA-3.0
