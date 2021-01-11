from tqdm import tqdm, trange
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np


df = pd.read_csv('combined_dataset.csv')
val = pd.read_csv('combined_dataset_validation.csv')

#['de', 'el', 'es', 'fr', 'it', 'sv']
lang = 'sv'
en2fr = df[df['language'] == lang]
ef2fr2 = val[val['language'] == lang]

en2fr = pd.concat([en2fr, ef2fr2]).reset_index()
en2fr = en2fr.drop(columns = 'language')

en_data = en2fr['l1'].values
jp_data = en2fr['l2'].values

en_train, en_subtotal, jp_train, jp_subtotal = train_test_split(
        en_data, jp_data, test_size=.3, random_state=122)

en_test, en_val, jp_test, jp_val = train_test_split(
        en_subtotal, jp_subtotal, test_size=0.666, random_state=122)

file_mapping = {
    'train.en_XX': en_train,
    f'train.{lang}_XX': jp_train,
    'valid.en_XX': en_val,
    f'valid.{lang}_XX': jp_val,
    'test.en_XX': en_test,
    f'test.{lang}_XX': jp_test,
}

for k, v in file_mapping.items():
    np.savetxt(f'data/en2{lang}/{str(k)}', v, newline="\n", fmt='%s')



