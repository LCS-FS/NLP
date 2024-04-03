import pandas as pd
import pickle

lr = pd.read_csv('assign1/datasets/exploration/lr.csv')
sampled = pd.read_csv('assign1/datasets/small_data_sample.csv')

joined_lr = lr.join(sampled, lsuffix='_lr', rsuffix='_sampled')

filtered_lr = joined_lr[joined_lr['actual'] != joined_lr['predicted']]

filtered_lr.to_csv('assign1/datasets/exploration/lr_joined.csv')

svc = pd.read_csv('assign1/datasets/exploration/svc.csv')
with open('assign1/datasets/pickle/test_features_embeddes.pkl', 'rb') as f:
    test_features_embeddes = pickle.load(f)

embedds_pd = pd.DataFrame(test_features_embeddes)

joined_svc = svc.join(embedds_pd, lsuffix='_svc', rsuffix='_sampled')
joined_svc2 = joined_svc.join(sampled, lsuffix='_svc', rsuffix='_sampled')

with open('assign1/datasets/exploration/svc_joined.pkl', 'wb') as f:
    pickle.dump(joined_svc2, f)
    
print(joined_svc2.head())