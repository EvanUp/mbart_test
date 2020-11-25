import pandas as pd

df = pd.read_csv('data/combined_dataset.csv')
val = pd.read_csv('data/combined_dataset_validation.csv')

en2fr = df[df['language'] == 'fr']
ef2fr2 = val[val['language'] == 'fr']

df.language.unique()

en2fr = pd.concat([en2fr, ef2fr2]).reset_index()
en2fr = en2fr.drop(columns = 'language')
en2fr.to_csv("data/en2fr.tsv", sep="\t", header = None, index = False)


