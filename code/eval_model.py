from fairseq.models.bart import BARTModel
import torch
import pandas as pd
from tqdm import tqdm

df = pd.read_csv('test-enes.csv')
text = df.test.values
dummy = []

torch.device('cuda' if torch.cuda.is_available() else 'cpu')

bart = BARTModel.from_pretrained(
	'./',
	checkpoint_file='checkpoint_last.pt',
	bpe='sentencepiece',
	sentencepiece_model='./sentence.bpe.model')
bart.cuda()
bart.eval()

#sentence_list = ['Concomitant use of the following substances is contraindicated QTc-prolonging medicinal products o anti-arrhythmics class IA (e.g., disopyramide, hydroquinidine, quinidine)']

for i in tqdm(text):
	try:
		with torch.no_grad():
			dummy.append(bart.sample(str(i), beam=5))
	except:
		print('nope')
		dummy.append('NA')

df['final'] = dummy
df.to_csv('final_output.csv')

#translation = bart.sample(sentence_list, beam =5)
#print(translation)
#breakpoint()
