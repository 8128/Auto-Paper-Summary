Automatic Paper Summary
================
The goal of this project is to create a system which generates a short and accurate summary from longer text. We constructed a user friendly website for usage at the following link.
```bash
http://34.221.113.97:8000/
```
Short text summary is designed to generate a summary within a length of three thousands words. For anything longer than three thousand words, user can upload a .txt file. Short text and Long text examples are provided for trials. 

The results could differ under different methods and ratio. The ratio of the content could be higher using short text summary, thus more comprehensive. For long text summary, the ratio of content could be slighter, thus more tough to understand the whole article. 

Usage
================


Technology Selection
================
**Sprint 1 – Seq2Seq + GloVe**
The original research is based on Long Short Term Memory (LSTM) as core technique of  Tensorflow. This model can change words into vector forms as input and generate abstract summary as output through Seq2Seq Algorithm. GloVe is an unsupervised learning Algorithm for obtaining vector representations for words. 

**Sprint 2 – CoreNLP**
This is a natural language software provide by Stanford University. It provides numerous linguistics analysis tools but it wasn’t an ideal method for paper summarization after our testing.

**Sprint 3 – Gensim**
The Gensim implementation was based on popular “TextRank” Algorithm. This module automatically summarizes the given text, by extracting one or more important sentences from the text. This was so far the best approach for our project.

**Final - Django**


Website Building
================


Project Sprints
================
**Sprint 1**

**Sprint 2**

**Sprint 3**

**Final**

Challenges
================
**Dataset Selection**

  * Finding appropriate datasets was a very tough task. The biggest reason was because not many existed or similar experiments before
  * First stage of project was using Document Understanding Conference(DUC) 2003 and 2004 dataset. This dataset doesn't actually contain the summaries we could use to train our model. It also has bizarre instructions on the usage. Therefore, we moved on to the next selection. 
  * Next stage of project was using NIST 2015 dataset from Kaggle. This dataset contains summarized text that can train the model which is the most fitted dataset we've found so far. 

**Training Model**

  * Most of the datasets contain equations, graphs, pictures and charts. It’s hard to train the model for pure text summarization. We've tried a serveral ways to optimize this problem but garbled summaries were inevitable.
  
**Word Embedding**

  * Since we were using seq2seq method to create abstract summary but some terms in datasets are very rare. The model is hard to relate or recognize the words to form an accurate summary. 




First, we turn word into vectors which the computer should recognize. Second, we use the method of LSTM to train our label and vectors. This give us our model. Then, we turn the paper from the user into vectors and use it as the input of our model, we should get output vectors. At last, we turn the output vectors into words and print out the summary we make. 

For the website building part, we want to use Django based on Python. User can input a paper on our website and we are able to give them a summarization directly. For now, we prefer the default database sqlite3. If it fails to fulfill our needs, we would try MySQL.
