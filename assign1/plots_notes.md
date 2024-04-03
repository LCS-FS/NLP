Model  best value    best features to worst (in accuracy values)

NB     0.895         text_and_tokens, all_features/no_ner, embeddings, entities

LG     0.895         all_features/no_ner, embeddings, text_and_tokens, entities

DT     0.77          all_features, embeddings, no_ner, text_and_tokens, entities

RF     0.86          text_and_tokens, all_features/no_ner, embeddings, entities

SVM    0.895         embeddings, all_features, no_ner, text_and_tokens, entities

EGB    0.88          text_and_tokens, all_features, embeddings, no_ner, entities

GB     0.889         all_features/no_ner, embeddings, text_and_tokens, entities 

KNN    0.76          all_features/no_ner, text_and_tokens, embeddings, entities 


- no_ner (all features sem entities) nao apresentou diferenças relevantes relativamente a usar all_features - fazer grafico
- ambas as features text_and_tokens, all_features, embeddings e no_ner apresentam bons valores de accuracy
- entities apenas não revelou ser uma boa feature já que apresenta valores de accuracy muito mais baixos que o resto das features (fazer gráfico da accuracy de todos os models no mesmo plot)
- os modelos que dão melhores resultados são o NB, LG, SVS e GB. Os piores resultados são obtidos com o DT e o KNN
- o único gráfico em que as métricas apresentam valores mais distintos é no do knn model, em que valores de precision são superiores ao resto das métricas, possible justification here:
...KNN
Accuracy measures the overall correctness of the classifier, while precision focuses on the proportion of correctly predicted positive instances among all instances predicted as positive. Recall, on the other hand, emphasizes the proportion of correctly predicted positive instances among all actual positive instances. In situations where false positives are relatively low compared to true positives, precision may appear higher than recall.
The visually lower recall compared to precision and F1-score suggests that while the KNN model is precise in identifying positive instances, it might miss some positive instances present in the dataset. This could be due to the way KNN works, especially in regions where one class dominates over others.
Even though your dataset is perfectly balanced, the KNN algorithm might encounter regions in the feature space where one class dominates over the others. This imbalance can lead to instances of minority classes being misclassified more often.