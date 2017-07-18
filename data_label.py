import data_function as df
import os
import random
'''
# This script labels the wiki data sentences into positive (important sentences) and negative (unimportant)
# Currently use all introduction sentences as positive. Randomly choose same number of sentences from main content
# as negative
'''
if not os.path.isdir('./labeled'):
    os.mkdir('./labeled')
count=0
f_pos = open('./labeled/wiki_positive_0','w+')
f_neg = open("./labeled/wiki_negative_0",'w+')
for dict in df.get_wiki('./extracted'):
    if(count%400000==0):
        f_pos.close()
        f_neg.close()
        f_pos = open('./labeled/wiki_positive_'+str(int(count/400000)), 'w+')
        f_neg = open('./labeled/wiki_negative_'+str(int(count/400000)), 'w+')
    num_intro_lines=len(dict['introduction'])
    num_content_lines=len(dict['content'])
    if num_intro_lines<=num_content_lines:
        for line in dict['introduction']:
            line=df.clean_str(line,rm_stopwords=False)
            f_pos.write(line+'\n')
        for i in range(num_intro_lines):
            line=random.choice(dict['content'])
            line=df.clean_str(line,rm_stopwords=False)
            f_neg.write(line+'\n')
    count+=1
f_pos.close()
f_neg.close()