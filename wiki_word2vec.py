from gensim.models import Word2Vec
from data_function import get_filepaths

# sentence iterator
class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for fname in get_filepaths(self.dirname):
            print(fname)
            for line in open(fname):
                yield line.split()

# Train the word2vec model
# sentences = MySentences('./cleaned')
# model = Word2Vec(sentences,min_count=10)
# model.save('./wiki_model')

# Test the model
model = Word2Vec.load('./wiki_model')
word_list=['hu']
for word in word_list:
    print("most similar to word %s"%word)
    print(model.most_similar(positive=[word]))
print(model.wv.syn0.shape)