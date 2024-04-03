# NLP Assignment 1

## Group K Members

| Name | Number |
| --- | --- |
| Bárbara Rodrigues | 202007163 |
| Guilherme Pereira | 202007375 |
| Lucas Sousa | 202004682 |

## Dataset
The dataset can be found [here](https://www.kaggle.com/datasets/vrindakallu/ag-news-topic-classification)

## Execution

Order:
- exploration.ipynb
- preprocessing.ipynb (this one also contains the training and testing of the modules, due to the need to keep spacy variables in the same environment as the models)
- eval.ipynb (for testing models using count Vectorizer and TF-IDF Vectorizer, as well as preparing the best models for error analysis)
- filter.py
- embeds_analysis.ipynb

*Note 1: Due to the extensive size of the training dataset, only a third of it was used (40000 balanced entries)*
*Note 2: Execution of the preprocessing and eval notebooks requires several Gigabytes of RAM and storage, as well as several days of runtime*