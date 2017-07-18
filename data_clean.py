import data_function as df
import os
'''
# This script clean the raw text data which is extracted from wiki dump
# Including split wiki page into <Title> <Introduction> and <Content>, clean strings and optional remove stopwords
'''
if not os.path.isdir('./cleaned'):
    os.mkdir('./cleaned')
path='./cleaned/wiki_'
init=0
f = open(path+str(init),'w+')
for dict in df.get_wiki('./extracted'):
    if init%5000==0:
        f.close()
        f = open(path+str(int(init/5000)),'w+')
    f.write('<Title>\n')
    f.write(dict['title']+'\n')
    f.write('<Introduction>\n')
    for intro in dict['introduction']:
        intro=df.clean_str(intro,rm_stopwords=False)
        f.write(intro+'\n')
    f.write('<Content>\n')
    for content in dict['content']:
        content = df.clean_str(content,rm_stopwords=False)
        f.write(content+'\n')
    init+=1
f.close()