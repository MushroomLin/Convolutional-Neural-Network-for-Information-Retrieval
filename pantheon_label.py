import pandas as pd
import wikipedia
import os
import nltk
import random
'''
This script use data from MIT Pantheon project to generate training dataset of the CNN
'''
# Data label part
# create directory
if not os.path.isdir('./labeled'):
    os.mkdir('./labeled')
# create and open labeled file
count=0
f_pos = open('./labeled/wiki_positive','w+')
f_neg = open("./labeled/wiki_negative",'w+')


data=pd.read_csv('./pantheon.tsv',delimiter='\t')
ranked_data=data[['name','HPI']].sort_values(by='HPI',ascending=False)
print(ranked_data)

for name in ranked_data['name']:
    print(name)
    try:
        summary = wikipedia.summary(name)
        content = wikipedia.page(name).content
    except Exception:
        continue
    summary=nltk.sent_tokenize(summary)
    length=len(summary)
    content=nltk.sent_tokenize(content)
    for i in range(length):
        line_pos = summary[i]
        line_neg = random.choice(content)
        while ('=' in line_neg):
            line_neg=random.choice(content)
        f_pos.write(line_pos.strip())
        f_pos.write('\n')
        f_neg.write(line_neg.strip())
        f_neg.write('\n')

f_neg.close()
f_pos.close()