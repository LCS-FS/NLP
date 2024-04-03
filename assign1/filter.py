import pandas as pd

lr = pd.read_csv('assign1/datasets/exploration/lr.csv')
# svc = pd.read_csv('datasets/exploration/svc.csv')
sampled = pd.read_csv('assign1/datasets/small_data_sample.csv')

joined_lr = lr.join(sampled, lsuffix='_lr', rsuffix='_sampled')
# joined_svc = svc.join(sampled, lsuffix='_svc', rsuffix='_sampled')

filtered_lr = joined_lr[joined_lr['actual'] != joined_lr['predicted']]

filtered_lr.to_csv('assign1/datasets/exploration/lr_joined.csv')