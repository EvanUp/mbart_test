from tqdm import tqdm, trange
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

df = pd.read_csv('mbart_test/data/en2fr.csv', header=None)
en_data = df[1].values
jp_data = df[2].values

#en_data = [str(i) + '\n' for i in en_data]
#jp_data = [str(i) + '\n' for i in jp_data]

olen = ([len(str(x)) for x in en_data])

total_test = 60000
en_train, en_subtotal, jp_train, jp_subtotal = train_test_split(
        en_data, jp_data, test_size=total_test, random_state=122)

en_test, en_val, jp_test, jp_val = train_test_split(
        en_subtotal, jp_subtotal, test_size=0.5, random_state=122)

file_mapping = {
    'train.en_XX': en_train,
    'train.fr_XX': jp_train,
    'valid.en_XX': en_val,
    'valid.fr_XX': jp_val,
    'test.en_XX': en_test,
    'test.fr_XX': jp_test,
}

for k, v in file_mapping.items():
    np.savetxt(f'mbart_test/data/en2fr/{str(k)}', v, newline="\n", fmt='%s')