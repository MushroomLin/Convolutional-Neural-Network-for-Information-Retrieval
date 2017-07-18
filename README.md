# Convolutional-Neural-Network-for-Information-Retrieval
This is my summer research topic, trying to train convolutional neural network to analyze text data importance and retrieval important units.
## Usage
This project use Wikipedia data for training model.
To run these script you need :
  - Python 3.6
  - Tensorflow
  - Gensim
  - NLTK
  - Numpy
To run these script you should :
  - Download the Wikipedia whole dump at [HERE] (https://dumps.wikimedia.org)
  - Use WikiExtractor to extract text from xml format at [HERE] (https://github.com/bwbaugh/wikipedia-extractor)
  - Put extracted file into this folder at ./extracted
## File description
### data_function.py
Provides necessary functions for data processing and training.
### data_clean.py
Clean and rebuild raw data into title, introduction and content.
### data_label.py
Label sentences into positive and negative.
### wiki_cnn.py
Define the cnn model.
### wiki_cnn_train
Train the cnn model.
### wiki_cnn_eval.py
Evaluation the training and do testing.
### wiki_word2vec.py
Train a word2vec model for embedding text data into matrix

## Word2Vec Workflow:
- data_clean.py
- wiki_word2vec.py
## CNN Workflow:
- data_label.py
- wiki_cnn_train.py
- wiki_cnn_eval.py --eval_train --checkpoint_dir="./runs/your_number/checkpoints/"