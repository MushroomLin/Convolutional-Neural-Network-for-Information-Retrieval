import os
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
'''
This script provides functions for data processing
'''
def get_wiki(directory):
    """
    :param directory: input directory
    :return: a dir with key 'title', 'introduction', 'content'
    """
    for file in get_filepaths(directory):
        print(file)
        # Open file
        f=open(file,'r')
        content=f.read()
        # Compile regular expressions
        splitter = re.compile(r'</doc>')
        paragraph_splitter = re.compile(r'\n+')
        header = re.compile(r'<doc.*>')
        # Go through the file to get different part of the file
        # Separate the data into title, introduction and content
        for page in re.split(splitter, content):
            head = re.search(header, page)
            if head:
                page = page.replace(head.group(0), '')
                count = 0
                wiki = {}
                wiki['introduction'] = []
                wiki['content'] = []
                for paragraph in re.split(paragraph_splitter, page):
                    if paragraph:
                        if count == 0:
                            wiki['title'] = paragraph
                        elif count == 1:
                            sentence_intro = nltk.sent_tokenize(paragraph)
                            wiki['introduction'] += sentence_intro
                        else:
                            sentence_content = nltk.sent_tokenize(paragraph)
                            wiki['content'] += sentence_content
                        count += 1
                yield wiki

def get_filepaths(directory):
    """
    :param directory: where file stores
    :return: return a list of all files in directory
    """
    file_paths = []
    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.
    return file_paths

def remove_stop_words(sentence):
    """
    :param sentence: input string
    :return: sentence after removing stop words
    """
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(sentence)
    filtered_words = [w for w in tokens if not w in stopwords.words('english')]
    return " ".join(filtered_words)

def clean_str(string, rm_stopwords = False):

    """
    Tokenization/string cleaning for all datasets except for SST.
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    """
    string=string.lower()

    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    if rm_stopwords:
        string=remove_stop_words(string)
        return string.strip()
    else:
        return string.strip()

def load_data_and_labels(positive_data_file, negative_data_file):
    """
    Loads MR polarity data from files, splits the data into words and generates labels.
    Returns split sentences and labels.
    """
    # Load data from files
    positive_examples = list(open(positive_data_file, "r").readlines())
    positive_examples = [s.strip() for s in positive_examples]
    negative_examples = list(open(negative_data_file, "r").readlines())
    negative_examples = [s.strip() for s in negative_examples]
    # Split by words
    x_text = positive_examples + negative_examples
    x_text = [clean_str(sent) for sent in x_text]
    # Generate labels
    positive_labels = [[0, 1] for _ in positive_examples]
    negative_labels = [[1, 0] for _ in negative_examples]
    y = np.concatenate([positive_labels, negative_labels], 0)
    return [x_text, y]


def batch_iter(data, batch_size, num_epochs, shuffle=True):
    """
    Generates a batch iterator for a dataset.
    """
    data = np.array(data)
    data_size = len(data)
    num_batches_per_epoch = int((len(data)-1)/batch_size) + 1
    for epoch in range(num_epochs):
        # Shuffle the data at each epoch
        if shuffle:
            shuffle_indices = np.random.permutation(np.arange(data_size))
            shuffled_data = data[shuffle_indices]
        else:
            shuffled_data = data
        for batch_num in range(num_batches_per_epoch):
            start_index = batch_num * batch_size
            end_index = min((batch_num + 1) * batch_size, data_size)
            yield shuffled_data[start_index:end_index]